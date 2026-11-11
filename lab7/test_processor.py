from hypothesis import given, strategies as st
from processor import process_order, calculate_total, validate_coupon

@given(st.text() | st.none(), st.integers() | st.none())
def test_process_order_no_crash(item, quantity):
    try:
        process_order(item, quantity)
    except Exception as e:
        assert False, f"process_order crashed with inputs ({item}, {quantity}) due to: {e}"

@given(st.lists(st.floats(allow_nan=False)) | st.none())
def test_calculate_total_no_crash(prices):
    try:
        calculate_total(prices)
    except Exception as e:
        assert Error, f"calculate_total crashed with input {prices} due to: {e}"

@given(st.text() | st.none())
def test_validate_coupon_no_crash(coupon):
    try:
        validate_coupon(coupon)
    except Exception as e:
        assert False, f"validate_coupon crashed with input {coupon} due to: {e}"