import allure

from locators.urls import URLS
from pages.main_page import Main_Page
from pages.order_page import Form_Order


class TestMainPage:

    @allure.title('Проверка кнопки заказа(верхняя)')
    @allure.feature('Check button(up)')
    @allure.story('Проверяем верхнюю кнопку заказать')
    def test_click_button_top(self, browser):
        main = Main_Page(browser)
        main.go_to_site()
        browser.refresh()
        main.put_off_cookie()
        main.click_to_order_top()
        assert browser.current_url == URLS.scooter_url

    @allure.title('Проверка кнопки заказа(нижняя)')
    @allure.feature('Check button(down)')
    @allure.story('Проверяем нижнюю кнопку заказать')
    def test_order_form_down(self, browser):
        order_form = Main_Page(browser)
        browser.refresh()
        order_form.click_to_order_down()
        fill_form = Form_Order(browser)
        fill_form.fill_name()
        fill_form.fill_address()
        fill_form.fill_phone()
        fill_form.click_continue_button()
        assert fill_form.text_arenda() == "Про аренду"

    @allure.title('Проверка кнопки "Самокат"')
    @allure.feature('Check button Scooter')
    @allure.story('Проверяем кнопку "Самокат"')
    def test_scooter_button(self, browser):
        click = Main_Page(browser)
        click.click_on_scooter_button()
        url = browser.current_url
        assert url == URLS.main_url
        text = click.check_scooter_button()
        assert text == 'Заказываете самокат'

    @allure.title('Проверка кнопки "Яндекс"')
    @allure.feature('Check button Yandex')
    @allure.story('Проверяем кнопку "Яндекс"')
    def test_yandex_button(self, browser):
        test_main_page = Main_Page(browser)
        browser.refresh()
        test_main_page.open_ya_page_by_logo()
        test_main_page.switch_to_another_tab()
        url = URLS()
        assert browser.current_url == url.ya_main_page_url







