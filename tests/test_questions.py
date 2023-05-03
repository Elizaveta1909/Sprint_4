import allure
from selenium.webdriver.common.by import By

from pages.questions_page import Question_Program
from locators.test_questions_locators import QuestionsLocators


class TestProgram:

    @allure.title('Тест первого вопроса')
    @allure.feature('First question')
    @allure.story('Проверяем первый вопрос')
    def test_first_question(self, browser):
        first_question = Question_Program(browser)  # Создаем экземпляр класса first_question
        first_question.go_to_site()  # Запускаем сайт
        browser.execute_script(QuestionsLocators.SCRIPT)  # Создаем скрипт
        first_question.do_first_question()  # Запускаем первый метод на проверку
        label = first_question.do_answer_first_question()  # Ответ на вопрос 1
        assert label.text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title('Тест второго вопроса')
    @allure.feature('Second question')
    @allure.story('Проверяем второй вопрос')
    def test_second_question(self, browser):
        second_question = Question_Program(browser)
        second_question.do_second_question()
        label = second_question.do_answer_second_question()  # Ответ на вопрос 2
        assert label.text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, " \
                             "можете просто сделать несколько заказов — один за другим."

    @allure.title('Тест третьего вопроса')
    @allure.feature('Third question')
    @allure.story('Проверяем третий вопрос')
    def test_third_question(self, browser):
        third_question = Question_Program(browser)
        third_question.do_third_question()
        label = third_question.do_answer_third_question()  # Ответ на вопрос 3
        assert label.text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. " \
                             "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. " \
                             "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title('Тест четвертого вопроса')
    @allure.feature('Fourth question')
    @allure.story('Проверяем четвертый вопрос')
    def test_fourth_question(self, browser):
        fourth_question = Question_Program(browser)
        fourth_question.do_fourth_question()
        label = fourth_question.do_answer_fourth_question()  # Ответ на вопрос 4
        assert label.text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title('Тест пятого вопроса')
    @allure.feature('Fifth question')
    @allure.story('Проверяем пятый вопрос')
    def test_fifth_question(self, browser):
        fifth_question = Question_Program(browser)
        fifth_question.do_fifth_question()
        label = fifth_question.do_answer_fifth_question()  # Ответ на вопрос 5
        assert label.text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по " \
                             "красивому номеру 1010."

    @allure.title('Тест шестого вопроса')
    @allure.feature('Sixth question')
    @allure.story('Проверяем шестой вопрос')
    def test_sixth_question(self, browser):
        sixth_question = Question_Program(browser)
        sixth_question.do_sixth_question()
        label = sixth_question.do_answer_sixth_question()  # Ответ на вопрос 6
        assert label.text == "Самокат приезжает к вам с полной зарядкой. " \
                             "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. " \
                             "Зарядка не понадобится."

    @allure.title('Тест седьмого вопроса')
    @allure.feature('Seventh question')
    @allure.story('Проверяем седьмой вопрос')
    def test_seventh_question(self, browser):
        seventh_question = Question_Program(browser)
        seventh_question.do_seventh_question()
        label = seventh_question.do_answer_seventh_question()  # Ответ на вопрос 7
        assert label.text == "Да, пока самокат не привезли. " \
                             "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title('Тест восьмого вопроса')
    @allure.feature('Eighth question')
    @allure.story('Проверяем восьмой вопрос')
    def test_eighth_question(self, browser):
        eighth_question = Question_Program(browser)
        eighth_question.do_eighth_question()
        label = eighth_question.do_answer_eighth_question()  # Ответ на вопрос 8
        assert label.text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
