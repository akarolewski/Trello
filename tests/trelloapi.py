import time

import requests

from common.config import get_trello_url, get_trello_api_key, get_trello_token
from common.helpers import generate_random_string
from common.httpstatus import OK


class TrelloApi:

    def __init__(self, url, key, token):
        self.url = url
        self.key = key
        self.token = token

    def create_board(self, board_name):
        url = self.url + '/1/boards'

        payload = {
            'key': self.key,
            'token': self.token,
            'name': board_name
        }

        response = requests.post(url, params=payload)

        print('CREATED BOARD: ', response.text)
        assert response.status_code == OK
        return response.json()['id']

    def create_list(self, name, board_id):
        url = self.url + '/1/lists'

        payload = {
            'key': self.key,
            'token': self.token,
            'name': name,
            'idBoard': board_id
        }

        response = requests.post(url, params=payload)

        print('CREATED LIST: ', response.text)
        assert response.status_code == OK
        return response.json()['id']

    def create_card(self, name, list_id):
        url = self.url + '/1/cards'

        payload = {
            'key': self.key,
            'token': self.token,
            'name': name,
            'idList': list_id
        }

        response = requests.post(url, params=payload)

        print('CREATED CARD: ', response.text)
        assert response.status_code == OK
        return response.json()['id']

    def update_card(self, description, cardId):
        url = self.url + f'/1/cards/{cardId}'

        payload = {
            'key': self.key,
            'token': self.token,
            'desc': description
        }

        response = requests.put(url, params=payload)

        print('UPDATED CARD: ', response.text)
        assert response.status_code == OK

    def delete_card(self, cardId):
        url = self.url + f'/1/cards/{cardId}'

        payload = {
            'key': self.key,
            'token': self.token
        }

        response = requests.delete(url, params=payload)

        print('DELETE CARD: ', response.text)
        assert response.status_code == OK

    def post_comment_on_card(self, comment, cardId):
        url = self.url + f'/1/cards/{cardId}/actions/comments'

        payload = {
            'key': self.key,
            'token': self.token,
            'text': comment
        }

        response = requests.post(url, params=payload)

        print('PUT A COMMENT ON A CARD: ', response.text)
        assert response.status_code == OK


BASE_URL = get_trello_url()
API_KEY = get_trello_api_key()
TOKEN = get_trello_token()
BOARD_NAME = generate_random_string(18)
LIST_NAME = generate_random_string(18)

FIRST_CARD_NAME = generate_random_string(14)
SECOND_CARD_NAME = generate_random_string(14)
THIRD_CARD_NAME = generate_random_string(14)

api = TrelloApi(BASE_URL, API_KEY, TOKEN)

created_board_id = api.create_board(BOARD_NAME)
created_list_id = api.create_list(BOARD_NAME, created_board_id)
time.sleep(1)

first_card_id = api.create_card(FIRST_CARD_NAME, created_list_id)
second_card_id = api.create_card(SECOND_CARD_NAME, created_list_id)
third_card_id = api.create_card(THIRD_CARD_NAME, created_list_id)

print(api.post_comment_on_card('New comment for test', first_card_id))
print(api.update_card('Description has been updated.', second_card_id))
print(api.delete_card(third_card_id))
