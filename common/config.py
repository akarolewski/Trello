import configparser

config = configparser.RawConfigParser()
config.read('../trello.cfg')


def get_trello_url():
    return config.get('trello', 'url')


def get_trello_api_key():
    return config.get('trello', 'apikey')


def get_trello_token():
    return config.get('trello', 'token')
