import pytest
import allure
from pages.home_page import HomePage
from utils.urls import Urls

@allure.epic('Эпик: Главная страница')
@allure.suite('Главная страница')
class TestHomePage:
    @allure.feature('Переход на страницу оформления заказа')
    @allure.story('Переход по кнопке \"Заказать\" в верхней части страницы')
    @allure.title('Клик по кнопке \"Заказать\" в header')
    def test_top_order_button_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_accept()
        home_page.click_top_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE, "Не произошел переход на страницу оформления заказа"

    @allure.feature('Переход на страницу оформления заказа')
    @allure.story('Переход по кнопке \"Заказать\" в нижней части страницы')
    @allure.title('Клик по кнопке \"Заказать\" в footer')
    def test_bottom_order_button_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_accept()
        home_page.click_bottom_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE, "Не произошел переход на страницу оформления заказа"

    @allure.feature('Переход на страницу Яндекс.Дзен')
    @allure.story('Редирект по кнопке Яндекс')
    @allure.title('Клик по логотипу Яндекс')
    def test_yandex_redirect(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_accept()
        home_page.click_yandex_button()
        home_page.switch_window(1)
        assert Urls.YANDEX_HOME_PAGE in home_page.current_url(), "Не произошел редирект на Яндекс"
