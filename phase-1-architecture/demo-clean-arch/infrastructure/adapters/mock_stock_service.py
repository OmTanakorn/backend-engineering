from decimal import Decimal
from application.ports.stock_service import StockService

class MockStockService(StockService):
    def __init__(self, initial_stock: dict[str, tuple[int, Decimal]] | None = None):
        # {product_id: (quantity, unit_price)}
        self.inventory = initial_stock or {
            "prod-laptop": (10, Decimal(35000)),
            "prod-mouse": (50, Decimal(890)),
            "prod-keyboard": (20, Decimal(2500)),
        }
        self.reserved_log: list[tuple[str, int]] = []
        self.released_log: list[tuple[str, int]] = []

    def check_and_reserve(self, product_id: str, quantity: int) -> Decimal:
        if product_id not in self.inventory:
            raise ValueError(f"Product '{product_id}' not found")
        stock, price = self.inventory[product_id]
        if stock < quantity:
            raise ValueError(f"Insufficient stock for product '{product_id}'. Available: {stock}")
        self.inventory[product_id] = (stock - quantity, price)
        self.reserved_log.append((product_id, quantity))
        return price

    def release_stock(self, product_id: str, quantity: int) -> None:
        if product_id in self.inventory:
            stock, price = self.inventory[product_id]
            self.inventory[product_id] = (stock + quantity, price)
        self.released_log.append((product_id, quantity))
