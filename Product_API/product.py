from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_search_by_name():
    response = client.get("/products?name=iphone")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "iPhone 15"


def test_search_by_category():
    response = client.get("/products?category=shoes")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_search_by_min_price():
    response = client.get("/products?min_price=600000")

    assert response.status_code == 200

    for product in response.json():
        assert product["price"] >= 600000


def test_search_by_price_range():
    response = client.get(
        "/products?min_price=100000&max_price=200000"
    )

    assert response.status_code == 200

    for product in response.json():
        assert 100000 <= product["price"] <= 200000


def test_search_with_multiple_parameters():
    response = client.get(
        "/products?category=electronics&min_price=700000"
    )

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_invalid_min_price():
    response = client.get("/products?min_price=-5000")

    assert response.status_code == 422


def test_invalid_name():
    response = client.get("/products?name=x")

    assert response.status_code == 422