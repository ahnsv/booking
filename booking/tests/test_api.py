import json
from datetime import datetime

from booking.domain.booking import Booking


def test_create_booking(client):
    response = client.request(
        "post",
        url="/api/v1/booking/",
        json={
            "title": "test_booking_create_api",
            "time_range": {
                "start_at": "2021-12-10T11:44:13.439Z",
                "end_at": "2021-12-10T11:44:13.439Z",
            },
        },
    )

    assert response.status_code == 200


def test_list_booking(client):
    response = client.get("/api/v1/booking/")

    assert response.status_code == 200


def test_get_booking_info(client):
    response = client.get("/api/v1/booking/1")
    expected = Booking(
        title="test_booking",
        id_=1,
        start_at=datetime.strptime("2021-12-10T11:44:13.439Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
        end_at=datetime.strptime("2021-12-10T11:44:13.439Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
    )

    for key, value in json.loads(expected.json(by_alias=True, exclude_unset=True)).items():
        assert response.json()[key] == value


def test_update_booking(client):
    booking_id_to_update = 1
    response = client.put(
        f"/api/v1/booking/{booking_id_to_update}",
        json={
            "title": "test_booking_create_api",
            "time_range": {
                "start_at": str(datetime.utcnow()),
                "end_at": str(datetime.utcnow()),
            },
        },
    )
    assert response.status_code == 200


def test_delete_booking(client):
    booking_id_to_delete = 1
    response = client.delete(f"/api/v1/booking/{booking_id_to_delete}")
    assert response.status_code == 200
