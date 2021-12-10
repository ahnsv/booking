import pytest
from fastapi.testclient import TestClient

from booking.presentation.app import app


@pytest.fixture(scope="function")
def client():
    client_ = TestClient(app)
    client_.post(
        "/api/v1/booking/",
        json={
            "title": "test_booking",
            "time_range": {
                "start_at": "2021-12-10T11:44:13.439Z",
                "end_at": "2021-12-10T11:44:13.439Z",
            },
        },
    )
    return client_
