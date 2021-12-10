def test_create_booking(client):
    response = client.request(
        "post",
        url="/api/v1/booking/",
        json={
            "title": "test_booking",
            "time_range": {"start_at": "2021-12-10T11:44:13.439Z", "end_at": "2021-12-10T11:44:13.439Z"},
        },
    )

    assert response.status_code == 200


def test_list_booking(client):
    response = client.get("/api/v1/booking/")

    assert response.json() == []


def test_update_booking(client):
    assert False


def test_delete_booking(client):
    assert False
