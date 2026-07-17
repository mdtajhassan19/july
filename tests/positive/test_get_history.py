from utilities.api_client import get
from utilities.runtime_data import read_runtime
from utilities.data_reader import load_data
from utilities.schema_validator import validate_schema


def test_get_history(initialize):

    runtime = read_runtime()

    body = load_data()["history"]

    response = get(body["endpoint"])

    assert response.status_code == body["status_code"]

    response_json = response.json()

    # print(f"Get history response:   {response_json}")

    assert response_json["total_calculations"] == runtime["total_operations"]

    assert response_json["history"] == runtime["history"]

    validate_schema(response_json, body["schema"])