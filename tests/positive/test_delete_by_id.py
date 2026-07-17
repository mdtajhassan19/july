from utilities.api_client import delete
from utilities.runtime_data import read_runtime


def test_delete_by_id(initialize):

    runtime = read_runtime()

    # print(f"Runtime data delete by id: {runtime}")

    response = delete(f"/history/{runtime['multiply_id']}")

    response_json = response.json()

    assert response.status_code == 200

    assert response_json['message'] == f"Calculation ID {runtime['multiply_id']} deleted successfully."