from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/register",
        json={
            "username": "rita123",
            "email": "rita@gmail.com",
            "password": "Rita123!"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User registered successfully"
    assert data["username"] == "rita123"
    assert data["email"] == "rita@gmail.com"