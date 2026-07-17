from utilities.api_client import put
from utilities.runtime_data import read_runtime
from utilities.data_reader import load_data
from utilities.schema_validator import validate_schema


def test_update(initialize):

    runtime = read_runtime()

    # print(f"Runtime data of update: {runtime}")

    body = load_data()["update"]

    response = put(body["endpoint"].format(id=runtime["add_id"]), body["request"])

    assert response.status_code == body["expected"]["status_code"]

    response_json = response.json()

    assert response_json["message"] == body["expected"]["message"]

    assert response_json["calculation"]["result"] == body["expected"]["result"]

    validate_schema(response_json, body["schema"])