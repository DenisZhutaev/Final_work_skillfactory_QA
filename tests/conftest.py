from selenium.webdriver.chrome.service import Service
from pages.locators import Locators
from selenium import webdriver
from config import PATH
import pytest


@pytest.fixture()
def browser():
    """
    Функция-фикстура для инициализации браузера
    """
    # Режим прохождения тестов без открытия браузера Google Chrome
    service = Service(PATH)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

    # Режим прохождения тестов с открытием браузера Google Chrome
    # driver = Service(PATH)
    # driver = webdriver.Chrome(service=driver)
    # driver.maximize_window()
    # yield driver
    # driver.quit()


# создаем экземпляр класса, чтобы не создавать его в каждом тесте
@pytest.fixture()
def auth(browser):
    """
    Функция-фикстура для авторизации пользователя в приложении
    """
    auth = Locators(browser)
    return auth
