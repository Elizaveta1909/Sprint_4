import allure

from pages.order_page import Main_Page, Form_Order, About_Rent, YandexButton, URL
from pages.questions_page import Question_Program


class TestOrders:

    @allure.title('Проверка кнопки заказа(верхняя)')
    @allure.feature('Check button(up)')
    @allure.story('Проверяем верхнюю кнопку заказать')
    def test_click_button_top(self, browser):
        first_question = Question_Program(browser)
        first_question.go_to_site()
        main = Main_Page(browser)
        browser.refresh()
        main.click_to_order_top()
        main.put_off_cookie()

    @allure.title('Заполнение формы заказа')
    @allure.feature('Filling out form')
    @allure.story('Заполняем форму "Для кого самокат" и "Про аренду"')
    def test_fill_out_form(self, browser):
        write_in_form_1 = Form_Order(browser)
        write_in_form_1.fill_name()
        write_in_form_1.fill_address()
        write_in_form_1.fill_phone()
        write_in_form_1.click_continue_button()
        write_in_form_2 = About_Rent(browser)
        write_in_form_2.fill_date()
        write_in_form_2.fill_other()

    @allure.title('Проверка успешного оформления заказа(верхняя кнопка)')
    @allure.feature('Fill "for rent"(top button)')
    @allure.story('Проверяем успешное оформление заказа(верхняя кнопка)')
    def test_check_exe_of_the_order(self, browser):
        check = About_Rent(browser)
        assert check.check_up_buttom() == "Посмотреть статус"
        check.check_status()

    @allure.title('Проверка кнопки "Самокат"')
    @allure.feature('Check button Scooter')
    @allure.story('Проверяем кнопку "Самокат"')
    def test_scooter_button(self, browser):
        click = YandexButton(browser)
        click.click_on_scooter_button()
        url = browser.current_url
        assert url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка кнопки заказа(нижняя)')
    @allure.feature('Check button(down)')
    @allure.story('Проверяем нижнюю кнопку заказать')
    def test_order_form_down(self, browser):
        order_form = Main_Page(browser)
        order_form.click_to_order_down()
        fill_form = Form_Order(browser)
        fill_form.fill_name()
        fill_form.fill_address()
        fill_form.fill_phone()
        fill_form.click_continue_button()
        assert fill_form.text_arenda() == "Про аренду"

    @allure.title('Проверка оформления заказа(нижняя кнопка) ')
    @allure.feature('Fill "for rent"(down)')
    @allure.story('Проверяем оформление заказа(нижняя кнопка)"')
    def test_about_rent_down(self, browser):
        write_in_rent = About_Rent(browser)
        write_in_rent.fill_date()
        write_in_rent.fill_other()
        check = About_Rent(browser)
        check.find_arenda_button()
        assert check.find_arenda_button() == "Посмотреть статус"
        check.check_status()

    @allure.title('Проверка кнопки "Яндекс"')
    @allure.feature('Check button Yandex')
    @allure.story('Проверяем кнопку "Яндекс"')
    def test_yandex_button(self, browser):
        test_main_page = Main_Page(browser)
        test_main_page.open_ya_page_by_logo()
        test_main_page.switch_to_another_tab()
        url = URL()
        assert browser.current_url == url.ya_main_page_url


