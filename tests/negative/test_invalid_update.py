# from utilities.api_client import put


# def test_invalid_update():

#     body={

#         "a":10,

#         "b":20,

#         "operation":"power"
#     }

#     response=put("/history/1",body)

#     assert response.status_code==400

from utilities.api_client import put
from utilities.runtime_data import read_runtime
from utilities.data_reader import load_data
from utilities.schema_validator import validate_schema


def test_invalid_update(initialize):

    runtime = read_runtime()

    body = load_data()["negative"]["invalid_operation"]

    response = put(

        f"/history/{runtime['add_id']}",

        {
            "a": body["a"],
            "b": body["b"],
            "operation": body["operation"]
        }
    )

    assert response.status_code == body["expected_status"]

    response_json = response.json()

    assert response_json["detail"] == body["expected_message"]

    validate_schema(response_json, "schemas/error/error_schema.json")