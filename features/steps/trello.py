from behave import *

from common.browser import browser
from common.config import TRELLO_USERNAME


@when('I type in username')
def type_in_username(context):
    browser.send_keys(TRELLO_USERNAME, "//input[@id='user']")


@when('I type in password')
def type_in_password(context):
    pass


@when('I press submit login button')
def submit_logn_button(context):
    pass


@then('I make sure that Im logged in')
def submit_logn_button(context):
    pass
