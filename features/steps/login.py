from behave import given, when
from selenium.webdriver.common.by import By

from common.config import TRELLO_USERNAME
from common.browser import browser


@given('I open Trello login page')
def open_login_page(context):
    browser.maximize()
    browser.navigate_to_login_page()


@when('I log in to the application')
def log_in_to_the_application(context):
    pass
