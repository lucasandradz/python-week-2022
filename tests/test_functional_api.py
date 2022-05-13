from beerlog.api import api
from fastapi.testclient import TestClient

client = TestClient(api)


def test_add_beer_from_api():
    response = client.post(
        "/beers",
        json={"name": "Beer", "style": "Style", "flavor": 1, "image": 1, "cost": 1},
    )
    responseBody = response.json()

    assert response.status_code == 200
    assert responseBody["id"] == 1
    assert responseBody["name"] == "Beer"
