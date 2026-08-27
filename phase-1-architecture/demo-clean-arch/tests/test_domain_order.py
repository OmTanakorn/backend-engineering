import pytest
from decimal import Decimal
from domain.order import Order, OrderStatus
from domain.exceptions import InvalidOrderStatusError, InsufficientQuantityError

def test_order_creation_valid():
    order = Order(id="1", product_id="p1", quantity=2, unit_price=Decimal(100))
    assert order.status == OrderStatus.PENDING
    assert order.calculate_total() == Decimal(200)

def test_order_with_discount():
    order = Order(id="1", product_id="p1", quantity=2, unit_price=Decimal(100))
    # 200 - 10% = 180
    assert order.calculate_total(discount_percent=Decimal(10)) == Decimal(180)

def test_order_invalid_quantity_raises_error():
    with pytest.raises(InsufficientQuantityError):
        Order(id="1", product_id="p1", quantity=0, unit_price=Decimal(100))

def test_mark_as_paid_success():
    order = Order(id="1", product_id="p1", quantity=1, unit_price=Decimal(100))
    order.mark_as_paid(charge_id="ch_123")
    assert order.status == OrderStatus.PAID
    assert order.charge_id == "ch_123"

def test_mark_as_paid_on_already_paid_order_fails():
    order = Order(id="1", product_id="p1", quantity=1, unit_price=Decimal(100))
    order.mark_as_paid(charge_id="ch_123")
    with pytest.raises(InvalidOrderStatusError):
        order.mark_as_paid(charge_id="ch_456")
