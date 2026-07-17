# from utilities.api_client import post


# def test_division_by_zero():

#     response=post(

#         "/divide",

#         {

#             "a":100,

#             "b":0
#         }

#     )

#     assert response.status_code==400

#     assert response.json()["detail"]=="Division by zero is not allowed."

# from utilities.api_client import post
# from utilities.data_reader import load_data


# def test_division_by_zero():

#     body = load_data()["negative"]["division_by_zero"]

#     response = post("/divide", body)

#     assert response.status_code == 400

from utilities.api_client import post
from utilities.data_reader import load_data
from utilities.schema_validator import validate_schema


def test_division_by_zero():

    body = load_data()["negative"]["division_by_zero"]

    response = post(
        "/divide",
        {
            "a": body["a"],
            "b": body["b"]
        }
    )

    assert response.status_code == body["expected_status"]

    response_json = response.json()

    assert response_json["detail"] == body["expected_message"]

    validate_schema(response_json, "schemas/error/error_schema.json")