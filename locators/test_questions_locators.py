from selenium.webdriver.common.by import By


class QuestionsLocators:
    LOCATOR_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # Кнопка Cookie
    LOCATOR_FIRST_QUESTION_BUTTON = (By.ID, "accordion__heading-0")
    LOCATOR_SECOND_QUESTION_BUTTON = (By.ID, "accordion__heading-1")
    LOCATOR_THIRD_QUESTION_BUTTON = (By.ID, "accordion__heading-2")
    LOCATOR_FOURTH_QUESTION_BUTTON = (By.ID, "accordion__heading-3")
    LOCATOR_FIFTH_QUESTION_BUTTON = (By.ID, "accordion__heading-4")
    LOCATOR_SIXTH_QUESTION_BUTTON = (By.ID, "accordion__heading-5")
    LOCATOR_SEVENTH_QUESTION_BUTTON = (By.ID, "accordion__heading-6")
    LOCATOR_EIGHTH_QUESTION_BUTTON = (By.ID, "accordion__heading-7")
    LOCATOR_ANSWER_Q_1 = [By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]"]
    LOCATOR_ANSWER_Q_2 = (By.CSS_SELECTOR, "#accordion__panel-1")
    LOCATOR_ANSWER_Q_3 = (By.CSS_SELECTOR, "#accordion__panel-2")
    LOCATOR_ANSWER_Q_4 = (By.CSS_SELECTOR, "#accordion__panel-3")
    LOCATOR_ANSWER_Q_5 = (By.CSS_SELECTOR, "#accordion__panel-4")
    LOCATOR_ANSWER_Q_6 = (By.CSS_SELECTOR, "#accordion__panel-5")
    LOCATOR_ANSWER_Q_7 = (By.CSS_SELECTOR, "#accordion__panel-6")
    LOCATOR_ANSWER_Q_8 = (By.CSS_SELECTOR, "#accordion__panel-7")
    SCRIPT = "window.scrollTo(0, document.body.scrollHeight);"
