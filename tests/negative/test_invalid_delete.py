# from utilities.api_client import delete


# def test_invalid_delete():

#     response=delete("/history/999")

#     assert response.status_code==404

from utilities.api_client import delete
from utilities.data_reader import load_data
from utilities.schema_validator import validate_schema


def test_invalid_delete():

    body = load_data()["negative"]["invalid_delete"]

    response = delete(f"/history/{body['id']}")

    assert response.status_code == body["expected_status"]

    response_json = response.json()

    assert response_json["detail"] == body["expected_message"]

    validate_schema(response_json, "schemas/error/error_schema.json")