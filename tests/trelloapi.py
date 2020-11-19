import requests
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
