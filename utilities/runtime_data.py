import json

RUNTIME_FILE = "testdata/runtime_data.json"


def write_runtime(data):

    with open(RUNTIME_FILE, "w") as file:
        json.dump(data, file, indent=4)


def read_runtime():

    with open(RUNTIME_FILE) as file:
        return json.load(file)