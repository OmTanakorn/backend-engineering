from dataclasses import dataclass
from enum import Enum
from decimal import Decimal
from domain.exceptions import InvalidOrderStatusError, InsufficientQuantityError

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    CANCELLED = "CANCELLED"

@dataclass
class Order:
    id: str | None
    product_id: str
    quantity: int
    unit_price: Decimal
    status: OrderStatus = OrderStatus.PENDING
    charge_id: str | None = None

    def __post_init__(self):
        if self.quantity <= 0:
            raise InsufficientQuantityError("Quantity must be greater than 0")
        if self.unit_price < Decimal(0):
            raise ValueError("Unit price cannot be negative")

    def calculate_total(self, discount_percent: Decimal = Decimal(0)) -> Decimal:
        raw_total = self.unit_price * self.quantity
        if discount_percent > Decimal(0):
            discount = raw_total * (discount_percent / Decimal(100))
            return raw_total - discount
        return raw_total

    def mark_as_paid(self, charge_id: str) -> None:
        if self.status != OrderStatus.PENDING:
            raise InvalidOrderStatusError(f"Cannot mark order with status {self.status} as PAID")
        if not charge_id:
            raise ValueError("charge_id is required")
        self.status = OrderStatus.PAID
        self.charge_id = charge_id

    def cancel(self) -> None:
        if self.status == OrderStatus.CANCELLED:
            raise InvalidOrderStatusError("Order is already cancelled")
        self.status = OrderStatus.CANCELLED
