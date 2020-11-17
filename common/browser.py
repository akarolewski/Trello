from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

from common.config import TRELLO_URL


class Browser:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Browser()
        return cls.instance

    def __init__(self):
        # if str(settings['browser']).lower() is "firefox":
        #     self.driver = webdriver.Firefox()
        # elif str(settings['browser']).lower() is "chrome":
        #     self.driver = webdriver.Chrome()
        # else:

        self.driver = webdriver.Chrome(ChromeDriverManager().download_and_install("2.43")[0])
        # self.driver = webdriver.Chrome("webdriver/chromedriver")

    def get_driver(self):
        return self.driver

    def get_element(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def get_elements(self, locator):
        return self.driver.find_elements(locator)

    def navigate_to_login_page(self):
        self.driver.get(TRELLO_URL + "/login")

    def maximize(self):
        self.driver.set_window_size(1920, 1080)

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 15).until(ec.presence_of_element_located((By.XPATH, locator)))

    def send_keys(self, text, locator):
        self.wait_for_element(locator)
        self.get_element(locator).send_keys(text)

    def click(self, locator):
        self.wait_for_element(locator)
        self.get_element(locator).click()


browser = Browser.get_instance()
