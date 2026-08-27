import uuid
from decimal import Decimal
from application.ports.payment_gateway import PaymentGateway

class MockPaymentGateway(PaymentGateway):
    def __init__(self):
        self.charges: dict[str, Decimal] = {}
        self.refunds: list[tuple[str, Decimal]] = []

    def charge(self, amount: Decimal, payment_token: str) -> str:
        if payment_token == "tok_fail":
            raise ValueError("Payment transaction declined by bank")
        charge_id = f"ch_{uuid.uuid4().hex[:10]}"
        self.charges[charge_id] = amount
        return charge_id

    def refund(self, charge_id: str, amount: Decimal) -> None:
        if charge_id not in self.charges:
            raise ValueError(f"Charge ID {charge_id} not found in gateway")
        self.refunds.append((charge_id, amount))
