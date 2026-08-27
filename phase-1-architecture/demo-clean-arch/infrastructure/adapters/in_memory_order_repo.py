import uuid
from domain.order import Order
from application.ports.order_repository import OrderRepository

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._storage: dict[str, Order] = {}

    def save(self, order: Order) -> Order:
        if not order.id:
            order.id = str(uuid.uuid4())[:8]
        self._storage[order.id] = order
        return order

    def get_by_id(self, order_id: str) -> Order | None:
        return self._storage.get(order_id)
