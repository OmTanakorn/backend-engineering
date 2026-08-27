from dataclasses import dataclass
from decimal import Decimal
from domain.order import Order
from application.ports.order_repository import OrderRepository
from application.ports.stock_service import StockService
from application.ports.payment_gateway import PaymentGateway

@dataclass(frozen=True)
class CreateOrderCommand:
    product_id: str
    quantity: int
    coupon_code: str | None
    payment_token: str

@dataclass(frozen=True)
class CreateOrderResult:
    order_id: str
    product_id: str
    quantity: int
    total_amount: Decimal
    status: str
    charge_id: str

class CreateOrderUseCase:
    def __init__(
        self,
        order_repo: OrderRepository,
        stock_service: StockService,
        payment_gateway: PaymentGateway,
    ):
        self.order_repo = order_repo
        self.stock_service = stock_service
        self.payment_gateway = payment_gateway

    def execute(self, command: CreateOrderCommand) -> CreateOrderResult:
        # 1. ตรวจสอบและสำรองสต็อก
        unit_price = self.stock_service.check_and_reserve(command.product_id, command.quantity)

        # 2. สร้าง Domain Entity
        order = Order(
            id=None,
            product_id=command.product_id,
            quantity=command.quantity,
            unit_price=unit_price
        )

        # 3. คำนวณส่วนลดตาม Business Rule
        discount_percent = Decimal(10) if command.coupon_code == "SUMMER10" else Decimal(0)
        total_amount = order.calculate_total(discount_percent=discount_percent)

        # 4. ชำระเงินผ่าน Payment Gateway Port
        charge_id = self.payment_gateway.charge(amount=total_amount, payment_token=command.payment_token)

        # 5. เปลี่ยนสถานะเป็นชำระเงินแล้วและบันทึกลง Repository
        order.mark_as_paid(charge_id=charge_id)
        saved_order = self.order_repo.save(order)

        return CreateOrderResult(
            order_id=saved_order.id or "",
            product_id=saved_order.product_id,
            quantity=saved_order.quantity,
            total_amount=total_amount,
            status=saved_order.status.value,
            charge_id=saved_order.charge_id or ""
        )
