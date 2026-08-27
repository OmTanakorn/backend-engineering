from typing import Protocol
from decimal import Decimal

class PaymentGateway(Protocol):
    def charge(self, amount: Decimal, payment_token: str) -> str:
        """Process charge and return transaction/charge ID."""
        ...

    def refund(self, charge_id: str, amount: Decimal) -> None:
        """Refund a previously charged transaction."""
        ...
