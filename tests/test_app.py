import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_client(client):
    response = client.post("/clients", json={
        "name": "Ravi",
        "age": 25,
        "program": "Fat Loss",
        "calories": 2000
    })
    assert response.status_code in [200, 201]


def test_get_clients(client):
    response = client.get("/clients")
    assert response.status_code == 200