import pytest
import allure
from pages.order_page import OrderPage
from utils.urls import Urls
from utils.test_data import YaScooterOrderPageData as order_data

@allure.epic('Эпик: Страница оформления заказа')
@allure.suite('Оформление заказа')
class TestOrderPage:
    @allure.feature('Проверка полей ввода')
    @allure.story('Ввод некорректного имени')
    @allure.title('Ошибка при вводе некорректного имени')
    def test_incorrect_first_name(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.input_first_name("123")
        order_page.go_next()
        assert order_page.is_error_displayed_for_first_name(), "Сообщение об ошибке не отображается"

    @allure.feature('Проверка полей ввода')
    @allure.story('Ввод некорректной фамилии')
    @allure.title('Ошибка при вводе некорректной фамилии')
    def test_incorrect_last_name(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.input_last_name("!@#")
        order_page.go_next()
        assert order_page.is_error_displayed_for_last_name(), "Сообщение об ошибке не отображается"

    @allure.feature('Проверка полей ввода')
    @allure.story('Ввод некорректного адреса')
    @allure.title('Ошибка при вводе некорректного адреса')
    def test_incorrect_address(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.input_address("123")
        order_page.go_next()
        assert order_page.is_error_displayed_for_address(), "Сообщение об ошибке не отображается"

    @allure.feature('Проверка полей ввода')
    @allure.story('Пустое поле метро')
    @allure.title('Ошибка при отсутствии выбора метро')
    def test_empty_subway_field(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.go_next()
        assert order_page.is_error_displayed_for_subway(), "Сообщение об ошибке не отображается"

    @allure.feature('Проверка полей ввода')
    @allure.story('Ввод некорректного номера телефона')
    @allure.title('Ошибка при вводе некорректного номера телефона')
    def test_incorrect_phone_number(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.input_telephone_number("abc")
        order_page.go_next()
        assert order_page.is_error_displayed_for_phone(), "Сообщение об ошибке не отображается"

    @allure.feature('Заполнение данных')
    @allure.story('Корректный ввод данных на этапе \"Для кого самокат\"')
    @allure.title('Успешное заполнение данных')
    def test_fill_user_data(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.fill_user_data(order_data.data_sets['data_set1'])
        order_page.go_next()
        assert order_page.is_on_rent_data_step(), "Не произошел переход на этап \"Про аренду\""

    @allure.feature('Заполнение данных')
    @allure.story('Оформление заказа')
    @allure.title('Проверка оформления заказа с корректными данными')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_complete_order(self, driver, data_set):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.fill_user_data(order_data.data_sets[data_set])
        order_page.go_next()
        order_page.fill_rent_data(order_data.data_sets[data_set])
        order_page.click_order()
        order_page.click_accept_order()
        order_number = order_page.get_order_number()
        assert len(order_number) > 0, "Номер заказа не был найден"
