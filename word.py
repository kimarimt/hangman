import requests


def get_word():
    response = requests.get('https://random-word-api.herokuapp.com/word')
    response.raise_for_status()

    return response.json()[0].lower()
