import pytest
from starlette.testclient import TestClient

from booking.presentation.app import app


@pytest.fixture(scope="function")
def client():
    client_ = TestClient(app)
    return client_
