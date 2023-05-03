import time

from BaseApp import BasePage
from locators.test_order_locators import OrderLocators
from locators.test_questions_locators import QuestionsLocators


class Main_Page(BasePage):
    def click_to_order_top(self):
        self.driverwait(OrderLocators.LOCATOR_TOP_ORDER_BUTTON).click()

    def click_to_order_down(self):
        self.driverwait(OrderLocators.LOCATOR_DOWN_ORDER_BUTTON).click()

    def search_down_bottom(self):
        self.driverwait(OrderLocators.LOCATOR_DOWN_BUTTOM)

    def put_off_cookie(self):
        self.driverwait(QuestionsLocators.LOCATOR_COOKIE_BUTTON).click()

    def switch_to_another_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        new_url = self.driver.current_url
        return new_url

    def open_ya_page_by_logo(self):
        self.driverwait(OrderLocators.LOGO_YANDEX).click()

    def click_on_yandex_button(self):
        self.driverwait(OrderLocators.LOCATOR_YANDEX_BUTTON).click()

    def click_on_scooter_button(self):
        self.driverwait(OrderLocators.LOCATOR_SCOOTER_BUTTON).click()

    def check_scooter_button(self):
        scooter = self.driverwait(OrderLocators.CHECK_BUTTON_SCOOTER)
        return scooter.text