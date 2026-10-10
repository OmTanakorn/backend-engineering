from dataclasses import dataclass

from application.ports.order_repository import OrderRepository
from application.ports.payment_gateway import PaymentGateway
from application.ports.stock_service import StockService
from domain.exceptions import InvalidOrderStatusError
from domain.order import OrderStatus


@dataclass(frozen=True)
class CancelOrderCommand:
    order_id: str


@dataclass(frozen=True)
class CancelOrderResult:
    order_id: str
    status: str
    refunded: bool


class CancelOrderUseCase:
    def __init__(
        self,
        order_repo: OrderRepository,
        stock_service: StockService,
        payment_gateway: PaymentGateway,
    ):
        self.order_repo = order_repo
        self.stock_service = stock_service
        self.payment_gateway = payment_gateway

    def execute(self, command: CancelOrderCommand) -> CancelOrderResult:
        # 1. ค้นหา Order
        order = self.order_repo.get_by_id(command.order_id)
        if not order:
            raise ValueError(f"Order {command.order_id} not found")

        # 2. ตรวจสอบสถานะและคืนเงินถ้าชำระแล้ว
        refunded = False
        if order.status == OrderStatus.PAID:
            if order.charge_id:
                total_amount = order.calculate_total()
                self.payment_gateway.refund(order.charge_id, total_amount)
                refunded = True

        # 3. คืนสต็อกสินค้า
        self.stock_service.release_stock(order.product_id, order.quantity)

        # 4. เปลี่ยนสถานะใน Domain และบันทึก
        order.cancel()
        self.order_repo.save(order)

        return CancelOrderResult(
            order_id=order.id or "", status=order.status.value, refunded=refunded
        )
