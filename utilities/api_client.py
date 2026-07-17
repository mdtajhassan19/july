import requests
from utilities.data_reader import load_data

data = load_data()

BASE_URL = data["base_url"]


def post(endpoint, body):
    return requests.post(BASE_URL + endpoint, json=body)


def get(endpoint):
    return requests.get(BASE_URL + endpoint)


def put(endpoint, body):
    return requests.put(BASE_URL + endpoint, json=body)


def delete(endpoint):
    return requests.delete(BASE_URL + endpoint)