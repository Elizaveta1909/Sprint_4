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

    def open(self):
        self.driver.get(OrderLocators.BASE_URL)

    def open_ya_page_by_logo(self):
        self.driverwait(OrderLocators.LOGO_YANDEX).click()

    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_url(self):
        return self.driver.current_url

class URL():
    ya_main_page_url = "https://dzen.ru/?yredirect=true"


class Form_Order(BasePage):
    # В fill_name заполняем имя и фамилию.
    def fill_name(self):
        self.driverwait(OrderLocators.LOCATOR_NAME_FORM).send_keys('Елизавета')
        self.driverwait(OrderLocators.LOCATOR_LASTNAME_FORM).send_keys('Первая')

    # В fill_address заполняем адрес и метро.
    def fill_address(self):
        self.driverwait(OrderLocators.LOCATOR_ADDRESS_FORM).send_keys('Улица Новый Арбат')
        self.driverwait(OrderLocators.LOCATOR_METRO_FORM_BUTTON).click()
        self.driverwait(OrderLocators.LOCATOR_METRO_SQUARE_BUTTON).click()

    # В fill_phone заполняем номер телефона и нажимаем далее.
    def fill_phone(self):
        self.driverwait(OrderLocators.LOCATOR_PHONE_FORM).send_keys('89612623265')

    def click_continue_button(self):
        self.driverwait(OrderLocators.LOCATOR_CONTINUE_BUTTON).click()

    def text_arenda(self):
        arenda = self.driverwait(OrderLocators.LOCATOR_TEXT_ARENDA)
        return arenda.text


# Класс About_Rent создан для окна "Про Аренду".
class About_Rent(BasePage):
    # В fill_date заполняем дату.
    def fill_date(self):
        self.driverwait(OrderLocators.LOCATOR_DATE_BRING_SCOOTER).send_keys('18.09.2022')
        self.driverwait(OrderLocators.LOCATOR_DATE_BRING_SCOOTER_BUTTON).click()
        self.driverwait(OrderLocators.LOCATOR_RENTAL_PERIOD_BUTTON).click()
        self.driverwait(OrderLocators.LOCATOR_RENTAL_PERIOD_CHOICE).click()

    # В fill_other заполняем цвет, комментарий, и нажимаем кнопку заказать, подтверждаем заказ.
    def fill_other(self):
        self.driverwait(OrderLocators.LOCATOR_COLOR_SCOOTER).click()
        self.driverwait(OrderLocators.LOCATOR_COMMENTARY).send_keys('Привести к 18:00.')
        self.driverwait(OrderLocators.LOCATOR_ORDER_BUTTON).click()
        self.driverwait(OrderLocators.LOCATOR_CONFIRM_BUTTON).click()

    # В check_status нажимаем на кнопку "проверить статус".
    def check_status(self):
        self.driverwait(OrderLocators.LOCATOR_CHECK_STATUS).click()

    def find_arenda_button(self):
        arenda_text = self.driverwait(OrderLocators.LOCATOR_CHECK_STATUS)
        return arenda_text.text

    def check_up_buttom(self):
        up_buttom = self.driverwait(OrderLocators.LOCATOR_UP_BOTTOM)
        return up_buttom.text


# Класс YandexButton создан для кнопок "Яндекс" и "Самокаты".
class YandexButton(BasePage):
    # В click_on_yandex_button мы нажимаем на кнопку "Яндекс".
    def click_on_yandex_button(self):
        self.driverwait(OrderLocators.LOCATOR_YANDEX_BUTTON).click()

    # В click_on_scooter_button мы нажимаем на кнопку "Самокаты".
    def click_on_scooter_button(self):
        self.driverwait(OrderLocators.LOCATOR_SCOOTER_BUTTON).click()