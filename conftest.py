import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--window-size=1200,800")

    driver = webdriver.Firefox(executable_path="./geckodriver")  # Задаем браузер
    # driver.maximize_window()  # Делаем полный экран

    yield driver  # Возвращаем генератор

    driver.quit()  # Выходим с браузера :)