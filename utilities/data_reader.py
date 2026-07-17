import json


def load_data():

    with open("testdata/calculator_data.json") as file:
        return json.load(file)