import pytest

import booking
import data
import helper
from booking import create_booking


def test_success_create_booking_name():
    body = helper.change_body_create("Jjjjj", "fieldfirst")
    actual_code = create_booking(body).status_code
    expected_code = 200
    assert actual_code == expected_code


def test_success_create_booking():
    pass


@pytest.mark.parametrize("total", [
    pytest.param(99999999, id="1 case Big price"),
    pytest.param(0.0001, id="2 small price"),
    pytest.param(123, id="3 case")
])
def test_success_create_book_price(total):
    body = helper.change_body_create(total, "totalprice")
    actual_code = test_success_create_booking()
    expected_code = 200
    assert actual_code == expected_code


def test_success_delete_book():
    response = booking.create_booking(data.body_create) # создали бронирование
    booking_id = response.json()["bookingid"]
    act_code = booking.delete_booking(booking_id).status_code
    exp_code = 201
    assert act_code == exp_code
