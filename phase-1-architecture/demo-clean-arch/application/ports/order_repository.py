from typing import Protocol
from domain.order import Order

class OrderRepository(Protocol):
    def save(self, order: Order) -> Order:
        """Persist an order to storage."""
        ...

    def get_by_id(self, order_id: str) -> Order | None:
        """Fetch an order by its unique ID."""
        ...
