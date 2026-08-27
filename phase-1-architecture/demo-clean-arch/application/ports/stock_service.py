from typing import Protocol
from decimal import Decimal

class StockService(Protocol):
    def check_and_reserve(self, product_id: str, quantity: int) -> Decimal:
        """
        Check if stock is available, reserve it, and return unit price.
        Raises ValueError or Exception if out of stock.
        """
        ...

    def release_stock(self, product_id: str, quantity: int) -> None:
        """Release reserved stock on order cancellation."""
        ...
