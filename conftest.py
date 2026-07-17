import pytest
from utilities.api_client import delete
from utilities.api_client import post
from utilities.runtime_data import write_runtime
from utilities.data_reader import load_data


@pytest.fixture(scope="function")
def initialize():

    data = load_data()
    # print(f"Load data: {data["add"][0]["request"]}")

    runtime = {}
    count = 0
    history = []

    response = post("/add", data["add"][0]["request"])
    runtime["add_id"] = response.json()["id"]
    history.append(response.json())
    count += 1

    response = post("/subtract", data["subtract"][0]["request"])
    runtime["subtract_id"] = response.json()["id"]
    history.append(response.json())
    count += 1

    response = post("/multiply", data["multiply"][0]["request"])
    runtime["multiply_id"] = response.json()["id"]
    history.append(response.json())
    count += 1

    response = post("/divide", data["divide"][0]["request"])
    runtime["divide_id"] = response.json()["id"]
    history.append(response.json())
    count += 1

    runtime["total_operations"] = count
    runtime["history"] = history

    write_runtime(runtime)

    yield runtime

    delete("/history")