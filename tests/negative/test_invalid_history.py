# from utilities.api_client import get


# def test_invalid_history():

#     response=get("/history/999")

#     assert response.status_code==404

#     assert response.json()["detail"]=="Calculation not found."

# from utilities.api_client import get
# from utilities.data_reader import load_data


# def test_invalid_history():

#     invalid_id = load_data()["negative"]["invalid_id"]

#     response = get(f"/history/{invalid_id}")

#     assert response.status_code == 404

from utilities.api_client import get
from utilities.data_reader import load_data
from utilities.schema_validator import validate_schema


def test_invalid_history():

    body = load_data()["negative"]["invalid_history"]

    response = get(f"/history/{body['id']}")

    assert response.status_code == body["expected_status"]

    response_json = response.json()

    assert response_json["detail"] == body["expected_message"]

    validate_schema(response_json, "schemas/error/error_schema.json")