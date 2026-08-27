import pytest
from decimal import Decimal
from domain.order import OrderStatus
from infrastructure.adapters.in_memory_order_repo import InMemoryOrderRepository
from infrastructure.adapters.mock_stock_service import MockStockService
from infrastructure.adapters.mock_payment_gateway import MockPaymentGateway
from application.use_cases.create_order import CreateOrderUseCase, CreateOrderCommand

def test_create_order_success_with_summer10_coupon():
    repo = InMemoryOrderRepository()
    stock = MockStockService({"prod-1": (5, Decimal(1000))})
    payment = MockPaymentGateway()

    use_case = CreateOrderUseCase(order_repo=repo, stock_service=stock, payment_gateway=payment)

    cmd = CreateOrderCommand(
        product_id="prod-1",
        quantity=2,
        coupon_code="SUMMER10",
        payment_token="tok_valid"
    )

    result = use_case.execute(cmd)

    # Assertions
    assert result.status == OrderStatus.PAID.value
    assert result.total_amount == Decimal(1800)  # (2000) - 10%
    assert result.order_id != ""
    assert stock.inventory["prod-1"][0] == 3  # 5 - 2 = 3

def test_create_order_out_of_stock_fails():
    repo = InMemoryOrderRepository()
    stock = MockStockService({"prod-1": (1, Decimal(1000))})
    payment = MockPaymentGateway()

    use_case = CreateOrderUseCase(order_repo=repo, stock_service=stock, payment_gateway=payment)

    cmd = CreateOrderCommand(
        product_id="prod-1",
        quantity=5,  # request 5 but have 1
        coupon_code=None,
        payment_token="tok_valid"
    )

    with pytest.raises(ValueError, match="Insufficient stock"):
        use_case.execute(cmd)

def test_create_order_payment_declined_fails():
    repo = InMemoryOrderRepository()
    stock = MockStockService({"prod-1": (10, Decimal(1000))})
    payment = MockPaymentGateway()

    use_case = CreateOrderUseCase(order_repo=repo, stock_service=stock, payment_gateway=payment)

    cmd = CreateOrderCommand(
        product_id="prod-1",
        quantity=1,
        coupon_code=None,
        payment_token="tok_fail"
    )

    with pytest.raises(ValueError, match="declined"):
        use_case.execute(cmd)
