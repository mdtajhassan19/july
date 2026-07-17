from utilities.api_client import get
from utilities.data_reader import load_data
from utilities.runtime_data import read_runtime
from utilities.schema_validator import validate_schema


def test_get_history_by_id(initialize):

    runtime = read_runtime()

    # print(f"Runtime data history by id: {runtime}")

    body = load_data()["history_by_id"]

    response = get(body["endpoint"].format(id=runtime["add_id"]))

    assert response.status_code == body["status_code"]

    response_json = response.json()

    # print(f"Get history by id response:   {response_json}")

    assert response_json["id"] == runtime["add_id"]

    id_history = next((item for item in runtime["history"] if item["id"] == runtime["add_id"]), None)

    # print(f"Add history:  {id_history}")

    assert response_json == id_history

    validate_schema(response_json, body["schema"])