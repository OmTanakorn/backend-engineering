import sys
from pathlib import Path
from decimal import Decimal

# Ensure project root is in python path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from infrastructure.adapters.in_memory_order_repo import InMemoryOrderRepository
from infrastructure.adapters.mock_stock_service import MockStockService
from infrastructure.adapters.mock_payment_gateway import MockPaymentGateway
from application.use_cases.create_order import CreateOrderUseCase, CreateOrderCommand
from application.use_cases.cancel_order import CancelOrderUseCase, CancelOrderCommand

def main():
    print("=" * 65)
    print("🚀 Clean Architecture & DDD - Order System Demo (Python)")
    print("=" * 65)

    # 1. Dependency Injection (Wiring Adapters to Ports)
    order_repo = InMemoryOrderRepository()
    stock_service = MockStockService()
    payment_gateway = MockPaymentGateway()

    create_order_uc = CreateOrderUseCase(order_repo, stock_service, payment_gateway)
    cancel_order_uc = CancelOrderUseCase(order_repo, stock_service, payment_gateway)

    # 2. Execute Create Order Use Case
    print("\n📦 [Action 1] Creating Order with coupon 'SUMMER10'...")
    cmd = CreateOrderCommand(
        product_id="prod-laptop",
        quantity=1,
        coupon_code="SUMMER10",
        payment_token="tok_visa_valid"
    )
    result = create_order_uc.execute(cmd)
    print(f"✅ Order Created Successfully!")
    print(f"   - Order ID     : {result.order_id}")
    print(f"   - Total Amount : {result.total_amount:,.2f} THB (Discounted 10%)")
    print(f"   - Status       : {result.status}")
    print(f"   - Charge ID    : {result.charge_id}")

    # 3. Check Order from Storage
    saved = order_repo.get_by_id(result.order_id)
    print(f"\n🔍 [Storage Check] Fetched Order {saved.id} -> Status: {saved.status.value}")

    # 4. Cancel Order Use Case
    print(f"\n↩️ [Action 2] Cancelling Order {result.order_id}...")
    cancel_cmd = CancelOrderCommand(order_id=result.order_id)
    cancel_res = cancel_order_uc.execute(cancel_cmd)
    print(f"✅ Order Cancelled Successfully!")
    print(f"   - Status   : {cancel_res.status}")
    print(f"   - Refunded : {cancel_res.refunded}")

    print("\n" + "=" * 65)
    print("🎉 All Clean Architecture layers executed cleanly!")
    print("=" * 65)

if __name__ == "__main__":
    main()
