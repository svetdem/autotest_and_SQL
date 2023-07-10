import data
import sender_stand_request


def get_order_track(body):
    order_track = sender_stand_request.post_new_order(body).json()["track"]
    return order_track


def test_get_new_order_by_track_success_response():
    created_order = sender_stand_request.post_new_order(data.order_body)
    track = created_order.json()[data.TRACK_FIELD]
    assert created_order.status_code == 201
    assert track != ""

    order_data = sender_stand_request.get_new_order_by_track(track)
    assert order_data.status_code == 200
