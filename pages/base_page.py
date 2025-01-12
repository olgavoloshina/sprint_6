import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def click_element(self, locator, time=10):
        element = self.find_element(locator, time)
        element.click()

    def input_text(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    @allure.step('Перейти по адресу {url}')
    def go_to_site(self, url):
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url
