import pytest
import allure
from pages.home_page import HomePage
from utils.test_data import YaScooterHomePageFAQ

@allure.epic('Эпик: FAQ на главной странице')
@allure.suite('FAQ')
class TestFAQ:
    @allure.feature('Раскрытие ответа в FAQ')
    @allure.story('Проверка, что при клике на вопрос FAQ отображается правильный ответ')
    @pytest.mark.parametrize(
        "question, answer, expected_answer",
        [
            (0, 0, YaScooterHomePageFAQ.answer1),
            (1, 1, YaScooterHomePageFAQ.answer2),
            (2, 2, YaScooterHomePageFAQ.answer3),
            (3, 3, YaScooterHomePageFAQ.answer4),
            (4, 4, YaScooterHomePageFAQ.answer5),
            (5, 5, YaScooterHomePageFAQ.answer6),
            (6, 6, YaScooterHomePageFAQ.answer7),
            (7, 7, YaScooterHomePageFAQ.answer8),
        ]
    )
    def test_faq_answer(self, driver, question, answer, expected_answer):
        home_page = HomePage(driver)
        home_page.go_to_site()
        home_page.click_cookie_accept()
        home_page.click_faq_question(question_number=question)
        faq_answer = home_page.find_element(Locators.FAQ_ANSWER(answer))
        assert faq_answer.is_displayed() and faq_answer.text == expected_answer, "Ответ не соответствует ожиданиям"
