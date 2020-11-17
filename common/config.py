import configparser

TRELLO_API = 'trello-api'
TRELLO = 'trello'

config = configparser.RawConfigParser()
config.read('trello.cfg')

TRELLO_API_URL = config.get(TRELLO_API, 'url')
TRELLO_API_KEY = config.get(TRELLO_API, 'apikey')
TRELLO_TOKEN = config.get(TRELLO_API, 'token')
TRELLO_URL = config.get(TRELLO, 'url')
TRELLO_USERNAME = config.get(TRELLO, 'email')
TRELLO_PASSWORD = config.get(TRELLO, 'password')
