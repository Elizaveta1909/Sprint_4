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

    def do_answer_first_question(self):
        question_1 = self.driverwait(QuestionsLocators.LOCATOR_ANSWER_Q_1)
        return question_1

    def do_answer_second_question(self):
        question_2 = self.driverwait(QuestionsLocators.LOCATOR_ANSWER_Q_2)
        return question_2

    def do_answer_third_question(self):
        question_3 = self.driverwait(QuestionsLocators.LOCATOR_ANSWER_Q_3)
        return question_3

    def do_answer_fourth_question(self):
        question_4 = self.driverwait(QuestionsLocators.LOCATOR_ANSWER_Q_4)
        return question_4

    def do_answer_fifth_question(self):
        question_5 = self.driverwait(QuestionsLocators.LOCATOR_ANSWER_Q_5)
        return question_5

    def do_answer_sixth_question(self):
        question_6 = self.driverwait(QuestionsLocators.LOCATOR_ANSWER_Q_6)
        return question_6

    def do_answer_seventh_question(self):
        question_7 = self.driverwait(QuestionsLocators.LOCATOR_ANSWER_Q_7)
        return question_7

    def do_answer_eighth_question(self):
        question_8 = self.driverwait(QuestionsLocators.LOCATOR_ANSWER_Q_8)
        return question_8
