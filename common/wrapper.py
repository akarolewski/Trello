from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdrivermanager import ChromeDriverManager


class Wrapper:

    def __init__(self):
        self._driver = None

    @property
    def driver(self):
        if not self._driver:
            return webdriver.Chrome(ChromeDriverManager().download_and_install()[0])
        return self._driver

    @staticmethod
    def wait_for_element(driver, locator):
        return WebDriverWait.until(driver, EC.visibility_of(locator))

    def get_element(self, driver):
        return driver
