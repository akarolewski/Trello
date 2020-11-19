from behave import *
from selenium.webdriver.support.select import Select

from common.browser import browser
from common.config import TRELLO_USERNAME, TRELLO_PASSWORD, BASE_URL, TRELLO_API_KEY, TRELLO_TOKEN
from common.strings.boarddata import BOARD_NAME, FIRST_COMMENT, SECOND_COMMENT
from common.strings.cardnames import FIRST_CARD_NAME, SECOND_CARD_NAME, THIRD_CARD_NAME
from tests.trelloapi import TrelloApi


def before_all(context):
    browser.maximize()


def after_all(context):
    browser.close()


@step('I create a new Trello Board')
def create_a_new_trello_board(context):
    context.api = TrelloApi(BASE_URL, TRELLO_API_KEY, TRELLO_TOKEN)
    context.created_board_id = context.api.create_board(BOARD_NAME)
    print(context.created_board_id)


@step('I create a new list')
def create_a_new_list(context):
    context.created_list_id = context.api.create_list(BOARD_NAME, context.created_board_id)


@step('I create a first card')
def create_a_first_card(context):
    context.first_card_id = context.api.create_card(FIRST_CARD_NAME, context.created_list_id)


@step('I create a second card')
def create_a_second_card(context):
    context.second_card_id = context.api.create_card(SECOND_CARD_NAME, context.created_list_id)


@step('I create a third card')
def create_a_third_card(context):
    context.third_card_id = context.api.create_card(THIRD_CARD_NAME, context.created_list_id)


@step('I post a comment on first card')
def post_a_comment_on_a_card(context):
    context.api.post_comment_on_card(FIRST_COMMENT, context.first_card_id)


@step('I update second card')
def update_a_card(context):
    context.api.update_card('Description has been updated.', context.second_card_id)


@step('I delete third card')
def delete_a_card(context):
    context.api.delete_card(context.third_card_id)


@step('I open Trello login page')
def open_login_page(context):
    browser.navigate_to_login_page()


@step('I type in username')
def type_in_username(context):
    browser.send_keys(TRELLO_USERNAME, "//input[@id='user']")


@step('I type in password')
def type_in_password(context):
    browser.wait_until_url_contains("https://id.atlassian.com/")
    browser.send_keys(TRELLO_PASSWORD, "//input[@id='password']")


@step('I press login button')
def submit_logn_button(context):
    browser.click("//input[@id='login']")


@step('I press submit login button')
def submit_logn_button(context):
    browser.get_element("//button[@id='login-submit']").submit()


@step('I make sure that Im logged in')
def submit_logn_button(context):
    browser.wait_until_url_contains("/board")


@step('I open recently added board')
def open_recently_added_board(context):
    browser.wait_until_url_contains("/board")
    browser.click(f"//a[@class='board-tile']//div[text() = '{BOARD_NAME}']")
    browser.wait_until_url_contains(f"{BOARD_NAME}")


@step('I make sure that two recently added cards are visible')
def make_sure_that_two_recently_added_cards_are_visible(context):
    browser.assert_amount_of_elements(2, "//a[contains(@class, 'list-card')]")


@step('I make sure that one card contains a comment')
def make_sure_one_card_contains_comment(context):
    browser.assert_amount_of_elements(1, "//span[contains(@class, 'icon-comment')]")


@step('I open that card\'s details page')
def open_cards_details_page(context):
    commented_card_xpath = "//span[contains(@class, 'icon-comment')]/ancestor::a[contains(@class, 'list-card')]"
    commented_card_href_value = browser.get_element(commented_card_xpath).get_attribute("href")
    browser.click(commented_card_xpath)
    browser.wait_until_url_contains(commented_card_href_value)
    browser.wait_for_element("//div[contains(@class, 'card-detail-window')]")


@step('I check whether previous comment contains correct message')
def check_added_comment_message(context):
    browser.assert_text_contained(
        FIRST_COMMENT, "//div[contains(@class, 'window-wrapper')]//div[contains(@class, 'action-comment')]")


@step('I add a comment to that card')
def add_a_comment_to_a_card(context):
    browser.send_keys(
        SECOND_COMMENT, "//div[contains(@class, 'comment-frame')]//textarea[contains(@class, 'comment-box-input')]")
    browser.click("//input[contains(@class, 'js-add-comment')]")


@step('I make sure that the comment has been added')
def assert_comment_has_been_added(context):
    browser.assert_amount_of_elements(
        2, "//div[contains(@class, 'js-list-actions')]//div[contains(@class, 'mod-comment-type')]")


@step('I set the card as done')
def set_the_card_as_done(context):
    browser.click("//a[contains(@class, 'js-move-card')]")
    browser.wait_for_element("//div[contains(@class, 'is-shown')]")

    select = Select(browser.get_element("//select[@class = 'js-select-list']"))
    select.select_by_visible_text('Done')
    browser.click("//input[contains(@class, 'js-submit')]")
