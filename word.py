import requests


def fetch_word():
    url = 'https://random-word-api.herokuapp.com/word'
    resp = requests.get(url)
    resp.raise_for_status()

    return resp.json()[0]
