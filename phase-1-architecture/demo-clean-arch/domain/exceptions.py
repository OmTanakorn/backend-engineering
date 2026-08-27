class DomainException(Exception):
    """Base exception for all domain-specific errors."""
    pass

class InvalidOrderStatusError(DomainException):
    """Raised when an operation is invalid for the current order status."""
    pass

class InsufficientQuantityError(DomainException):
    """Raised when order quantity is zero or negative."""
    pass
