from utilities.api_client import delete
from utilities.runtime_data import read_runtime


def test_delete_all(initialize):

    runtime = read_runtime()

    # print(f"Runtime data delete all: {runtime}")

    response = delete("/history")

    response_json = response.json()

    # print(f"Delete all: {response_json}")

    assert response.status_code==200

    assert response_json['message'] == "All calculation history deleted successfully."