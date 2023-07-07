from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL


class BasePage:
    """
    Этот класс представляет базовую страницу для всех остальных страниц.
    Он содержит общие методы, используемые на разных страницах.
    """

    def __init__(self, driver):
        """
        Конструктор класса BasePage.

        :param driver: объект Selenium WebDriver
        """
        self.driver = driver
        self.base_url = URL

    def go_to_site(self):
        """
        Переходит на базовый URL веб-сайта.

        :return: None
        """
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """
        Находит элемент на странице с использованием заданного локатора.

        :param locator: кортеж с стратегией и значением локатора
        :param time: максимальное время ожидания появления элемента (по умолчанию 10 секунд)
        :return: объект WebElement
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не удалось найти элемент по локатору {locator}"
        )

    def click_element(self, locator):
        """
        Нажимает на элемент, найденный по заданному локатору.

        :param locator: кортеж с стратегией и значением локатора
        :return: None
        """
        self.find_element(locator).click()

    def input_data(self, locator, text):
        """
        Вводит заданный текст в поле ввода, найденное по заданному локатору.

        :param locator: кортеж с стратегией и значением локатора
        :param text: текст для ввода в поле ввода
        :return: None
        """
        self.find_element(locator).send_keys(text)

    def out(self, driver):
        return self.driver.switch_to.window(driver.window_handles[1])
