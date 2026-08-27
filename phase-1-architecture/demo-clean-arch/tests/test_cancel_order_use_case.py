import pytest
from decimal import Decimal
from domain.order import Order, OrderStatus
from domain.exceptions import InvalidOrderStatusError
from infrastructure.adapters.in_memory_order_repo import InMemoryOrderRepository
from infrastructure.adapters.mock_stock_service import MockStockService
from infrastructure.adapters.mock_payment_gateway import MockPaymentGateway
from application.use_cases.cancel_order import CancelOrderUseCase, CancelOrderCommand

def test_cancel_paid_order_refunds_and_releases_stock():
    repo = InMemoryOrderRepository()
    stock = MockStockService({"prod-1": (8, Decimal(500))})
    payment = MockPaymentGateway()
    payment.charges["ch_test_123"] = Decimal(1000)

    # Prepare existing paid order in repository
    paid_order = Order(
        id="order-paid-1",
        product_id="prod-1",
        quantity=2,
        unit_price=Decimal(500),
        status=OrderStatus.PAID,
        charge_id="ch_test_123"
    )
    repo.save(paid_order)

    use_case = CancelOrderUseCase(order_repo=repo, stock_service=stock, payment_gateway=payment)
    cmd = CancelOrderCommand(order_id="order-paid-1")

    result = use_case.execute(cmd)

    assert result.status == OrderStatus.CANCELLED.value
    assert result.refunded is True
    assert ("ch_test_123", Decimal(1000)) in payment.refunds
    assert ("prod-1", 2) in stock.released_log
    assert stock.inventory["prod-1"][0] == 10  # 8 + 2

def test_cancel_already_cancelled_order_raises_error():
    repo = InMemoryOrderRepository()
    stock = MockStockService()
    payment = MockPaymentGateway()

    cancelled_order = Order(
        id="order-can-1",
        product_id="prod-1",
        quantity=1,
        unit_price=Decimal(100),
        status=OrderStatus.CANCELLED
    )
    repo.save(cancelled_order)

    use_case = CancelOrderUseCase(order_repo=repo, stock_service=stock, payment_gateway=payment)
    cmd = CancelOrderCommand(order_id="order-can-1")

    with pytest.raises(InvalidOrderStatusError):
        use_case.execute(cmd)
