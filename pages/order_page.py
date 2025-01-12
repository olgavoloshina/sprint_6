import allure
from pages.base_page import BasePage
from utils.locators import YaScooterOrderPageLocator as Locators

class OrderPage(BasePage):
    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name: str):
        self.input_text(Locators.LAST_NAME_INPUT, last_name)

    @allure.step('Ввод имени')
    def input_first_name(self, first_name: str):
        self.input_text(Locators.FIRST_NAME_INPUT, first_name)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        self.input_text(Locators.ADDRESS_INPUT, address)

    @allure.step('Выбор метро')
    def choose_subway(self, subway_name: str):
        self.click_element(Locators.SUBWAY_FIELD)
        self.click_element(Locators.SUBWAY_HINT_BUTTON(subway_name))

    @allure.step('Ввод номера телефона')
    def input_telephone_number(self, telephone_number: str):
        self.input_text(Locators.TELEPHONE_NUMBER_FIELD, telephone_number)

    @allure.step('Перейти на следующий этап заказа')
    def go_next(self):
        self.click_element(Locators.NEXT_BUTTON)

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        self.input_text(Locators.DATE_FIELD, date)

    @allure.step('Выбор периода аренды')
    def choose_rental_period(self, option: int):
        self.click_element(Locators.RENTAL_PERIOD_FIELD)
        self.find_elements(Locators.RENTAL_PERIOD_LIST)[option].click()

    @allure.step('Выбор цвета')
    def choose_color(self, option: int):
        self.find_elements(Locators.COLOR_CHECKBOXES)[option].click()

    @allure.step('Комментарий для курьера')
    def input_comment(self, comment_text):
        self.input_text(Locators.COMMENT_FOR_COURIER_FIELD, comment_text)

    @allure.step('Нажать \"Заказать\"')
    def click_order(self):
        self.click_element(Locators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def click_accept_order(self):
        self.click_element(Locators.ACCEPT_ORDER_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        about_order_text = self.find_element(Locators.ORDER_COMPLETED_INFO).text
        return ''.join(re.findall('[0-9]', about_order_text))

    @allure.step('Перейти к статусу заказа')
    def click_go_to_status(self):
        self.click_element(Locators.SHOW_STATUS_BUTTON)

    @allure.step('Заполнить данные на этапе \"Для кого самокат\"')
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.choose_subway(data_set['subway_name'])
        self.input_telephone_number(data_set['telepthone_number'])

    @allure.step('Заполнить данные на этапе \"Про аренду\"')
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rental_period'])
        for option in data_set['color']:
            self.choose_color(option)
        self.input_comment(data_set['comment_for_courier'])
