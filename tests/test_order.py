import allure

from pages.main_page import Main_Page
from pages.order_page import Form_Order, About_Rent



class TestOrders:

    @allure.title('Заполнение формы заказа')
    @allure.feature('Filling out form')
    @allure.story('Заходим на сайт, заполняем форму "Для кого самокат" и "Про аренду"')
    def test_fill_out_form(self, browser):
        main = Main_Page(browser)
        main.go_to_site()
        main.put_off_cookie()
        main.click_to_order_top()
        write_in_form_1 = Form_Order(browser)
        write_in_form_1.fill_name()
        write_in_form_1.fill_address()
        write_in_form_1.fill_phone()
        write_in_form_1.click_continue_button()
        write_in_form_2 = About_Rent(browser)
        write_in_form_2.fill_date()
        write_in_form_2.fill_other()
        assert write_in_form_2.check_up_buttom() == "Посмотреть статус"

    @allure.title('Проверка успешного оформления заказа(верхняя кнопка)')
    @allure.feature('Fill "for rent"(top button)')
    @allure.story('Проверяем успешное оформление заказа(верхняя кнопка)')
    def test_check_exe_of_the_order(self, browser):
        check = About_Rent(browser)
        button = check.check_status()
        assert button == 'Отменить заказ'  # Проверить, что видна кнопка "Отменить заказ"



