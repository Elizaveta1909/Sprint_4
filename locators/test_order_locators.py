from selenium.webdriver.common.by import By


class OrderLocators:

    LOGO_YANDEX = [By.CSS_SELECTOR, "[alt = 'Yandex']"]  #

    CANCEL_ORDER = [By.XPATH, "//button[contains(text(),'Отменить заказ')]"]

    LOCATOR_TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")  # Кнопка заказа(верхняя)

    LOCATOR_DOWN_ORDER_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM") # Кнопка заказа(нижняя)

    LOCATOR_NAME_FORM = (By.XPATH, "//input[@placeholder = '* Имя']")

    LOCATOR_LASTNAME_FORM = (By.XPATH, "//input[@placeholder = '* Фамилия']")  # Поле для ввода фамилии

    LOCATOR_ADDRESS_FORM = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(3) > input:nth-child(1)")

    LOCATOR_METRO_FORM_BUTTON = (By.CLASS_NAME, "select-search__input")  # Кнопка указания метро

    LOCATOR_METRO_SQUARE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[3]/button") # Выбор метро

    LOCATOR_PHONE_FORM = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")  # Кнопка для ввода номера телефона

    LOCATOR_CONTINUE_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM")  # Кнопка 'Далее'

    # продолжить(форма заказа)
    LOCATOR_DATE_BRING_SCOOTER = (By.XPATH, "//div[@class='react-datepicker__input-container']//input[@type='text']")  # Поле для ввода даты

    LOCATOR_DATE_BRING_SCOOTER_BUTTON = (By.CLASS_NAME, "react-datepicker__day--005")  # Подтверждение# даты в datepicker

    LOCATOR_RENTAL_PERIOD_BUTTON = (By.XPATH, "//div[@class='Dropdown-control']")  # Кнопка выбора периода времени катания

    LOCATOR_RENTAL_PERIOD_CHOICE = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(1)")  # Выбираем период времени

    LOCATOR_COLOR_SCOOTER = (By.CLASS_NAME, "Checkbox_Input__14A2w")  # Выбираем цвет самоката

    LOCATOR_COMMENTARY = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")  # Поле для ввода комментария

    LOCATOR_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") # Кнопка заказать в форме "заказа"

    LOCATOR_CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")  # Кнопка подтверждения заказа

    LOCATOR_CHECK_STATUS = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")  # Кнопка проверить статус

    LOCATOR_YANDEX_BUTTON = (By.XPATH, "//a [@href = '//yandex.ru']")

    LOCATOR_SCOOTER_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Кнопка "Самокаты"

    CHECK_BUTTON_SCOOTER = (By.XPATH, "//div[contains(text(),'Заказываете самокат')]")

    LOCATOR_UP_BOTTOM = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")  # Кнопка "Посмотреть статус"

    LOCATOR_DOWN_BUTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")

    LOCATOR_TEXT_ARENDA = (By.CLASS_NAME, "Order_Header__BZXOb")

