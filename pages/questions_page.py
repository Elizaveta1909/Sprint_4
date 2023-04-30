from BaseApp import BasePage
from locators.test_questions_locators import QuestionsLocators


class Question_Program(BasePage):
    def do_first_question(self):
        self.driverwait(QuestionsLocators.LOCATOR_COOKIE_BUTTON).click()
        self.driverwait(QuestionsLocators.LOCATOR_FIRST_QUESTION_BUTTON).click()

    # В данных методах реализуем нажатие на кнопки. В первом еще убираем надпись про куки
    def do_second_question(self):
        self.driverwait(QuestionsLocators.LOCATOR_SECOND_QUESTION_BUTTON).click()

    def do_third_question(self):
        self.driverwait(QuestionsLocators.LOCATOR_THIRD_QUESTION_BUTTON).click()

    def do_fourth_question(self):
        self.driverwait(QuestionsLocators.LOCATOR_FOURTH_QUESTION_BUTTON).click()

    def do_fifth_question(self):
        self.driverwait(QuestionsLocators.LOCATOR_FIFTH_QUESTION_BUTTON).click()

    def do_sixth_question(self):
        self.driverwait(QuestionsLocators.LOCATOR_SIXTH_QUESTION_BUTTON).click()

    def do_seventh_question(self):
        self.driverwait(QuestionsLocators.LOCATOR_SEVENTH_QUESTION_BUTTON).click()

    def do_eighth_question(self):
        self.driverwait(QuestionsLocators.LOCATOR_EIGHTH_QUESTION_BUTTON).click()