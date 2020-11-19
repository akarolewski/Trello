import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

from common.config import TRELLO_URL

CHROME_VERSION = "2.44"


class Browser:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Browser()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().download_and_install(CHROME_VERSION)[0])

    def get_driver(self):
        return self.driver

    def get_element(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def get_elements(self, locator):
        return self.driver.find_elements_by_xpath(locator)

    def navigate_to_login_page(self):
        self.driver.get(TRELLO_URL + "/login")

    def maximize(self):
        self.driver.maximize_window()

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((By.XPATH, locator)))
        self.wait_for_seconds(0.5)

    def wait_until_url_contains(self, text):
        WebDriverWait(self.driver, 15).until(ec.url_contains(text))
        self.wait_for_seconds(0.5)

    def send_keys(self, text, locator):
        self.wait_for_element(locator)
        self.get_element(locator).send_keys(text)

    def click(self, locator):
        self.wait_for_element(locator)
        self.get_element(locator).click()

    def assert_amount_of_elements(self, amount, locator):
        self.wait_for_element(locator)
        assert len(self.get_elements(locator)) == amount

    def get_text(self, locator):
        self.wait_for_element(locator)
        return self.get_element(locator).text

    def assert_text_contained(self, text, locator):
        self.wait_for_element(locator)
        assert text in self.get_text(locator)

    @staticmethod
    def wait_for_seconds(seconds):
        time.sleep(seconds)


browser = Browser.get_instance()
