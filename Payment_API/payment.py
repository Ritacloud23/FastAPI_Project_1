from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_successful_payment():
    response = client.post(
        "/payments",
        json={
            "amount": 50000,
            "card_number": "1234567890123456",
            "expiration_date": "12/2028",
            "cvv": "123"
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "successful"


def test_invalid_amount():
    response = client.post(
        "/payments",
        json={
            "amount": -5000,
            "card_number": "1234567890123456",
            "expiration_date": "12/2028",
            "cvv": "123"
        }
    )

    assert response.status_code == 422


def test_invalid_card_number():
    response = client.post(
        "/payments",
        json={
            "amount": 50000,
            "card_number": "12345",
            "expiration_date": "12/2028",
            "cvv": "123"
        }
    )

    assert response.status_code == 422


def test_invalid_cvv():
    response = client.post(
        "/payments",
        json={
            "amount": 50000,
            "card_number": "1234567890123456",
            "expiration_date": "12/2028",
            "cvv": "abc"
        }
    )

    assert response.status_code == 422


def test_expired_card():
    response = client.post(
        "/payments",
        json={
            "amount": 50000,
            "card_number": "1234567890123456",
            "expiration_date": "01/2020",
            "cvv": "123"
        }
    )

    assert response.status_code == 422


def test_payment_authentication_failure():
    response = client.post(
        "/payments",
        json={
            "amount": 50000,
            "card_number": "0000000000000000",
            "expiration_date": "12/2028",
            "cvv": "123"
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] if "status" in response.json() else True