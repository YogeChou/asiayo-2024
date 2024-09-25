import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="function")
def test_client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def order():
    return {
        "id": "A00001",
        "name": "Summer ABC",
        "address": {
            "city": "Taipei",
            "district": "Da An District",
            "street": "Xinyi Road"
        },
        "price": 1500.2,
        "currency": "USD"
    }
