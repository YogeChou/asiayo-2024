import pytest
from app.schemas import Order


def test_order_name_ok():
    valid_name = "Valid Order Name"
    assert Order.validate_name(valid_name) == valid_name


def test_order_name_contains_digit():
    with pytest.raises(ValueError) as exc_info:
        Order.validate_name("abc123")

    assert str(exc_info.value) == "Name contains non-English characters"


def test_order_name_contains_symbol():
    with pytest.raises(ValueError) as exc_info:
        Order.validate_name("abc#$*yz")

    assert str(exc_info.value) == "Name contains non-English characters"


def test_order_name_lowercase():
    with pytest.raises(ValueError) as exc_info:
        Order.validate_name("invalid order name")

    assert str(exc_info.value) == "Name is not capitalized"


def test_order_price_ok():
    valid_price = 999
    assert Order.validate_price(valid_price) == valid_price


def test_order_price_exceed():
    with pytest.raises(ValueError) as exc_info:
        Order.validate_price(3000)

    assert str(exc_info.value) == "Price is over 2000"


def test_order_currency_ok():
    assert Order.validate_currency("TWD") == "TWD"
    assert Order.validate_currency("USD") == "USD"


def test_order_currency_unknown():
    with pytest.raises(ValueError) as exc_info:
        Order.validate_currency("JPD")

    assert str(exc_info.value) == "Currency format is wrong"
