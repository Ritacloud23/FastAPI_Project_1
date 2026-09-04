from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_vehicle_by_id():
    response = client.get("/vehicles/2")

    assert response.status_code == 200
    assert response.json()["make"] == "Honda"
    assert response.json()["model"] == "Accord"


def test_vehicle_not_found():
    response = client.get("/vehicles/100")

    assert response.status_code == 404


def test_invalid_vehicle_id():
    response = client.get("/vehicles/abc")

    assert response.status_code == 422


def test_search_by_make():
    response = client.get("/vehicles?make=Toyota")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_search_by_model():
    response = client.get("/vehicles?model=Camry")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_search_by_price_range():
    response = client.get(
        "/vehicles?min_price=15000000&max_price=20000000"
    )

    assert response.status_code == 200


def test_search_with_multiple_parameters():
    response = client.get(
        "/vehicles?make=Toyota&model=Camry"
    )

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_invalid_price():
    response = client.get(
        "/vehicles?min_price=-5000"
    )

    assert response.status_code == 422