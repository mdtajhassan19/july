"""
    This test case is desige for performing addition operation
"""
import pytest

from utilities.data_reader import load_data
from utilities.api_client import post
from utilities.schema_validator import validate_schema

data = load_data()["add"]


@pytest.mark.parametrize("body", data)
def test_add(body):

    response = post(body["endpoint"], body["request"])

    assert response.status_code == body["expected"]["status_code"]

    response_json = response.json()

    # print(f"Test add: {response_json}")

    assert response_json["operation"] == body["expected"]["operation"]

    assert response_json["result"] == body["expected"]["result"]

    validate_schema(response_json, body["schema"])