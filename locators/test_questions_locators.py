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
    SCRIPT = "window.scrollTo(0, document.body.scrollHeight);"
