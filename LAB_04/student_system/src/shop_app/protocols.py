from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from shop_app.value_objects import Money


class EntityWithId(Protocol):
    """Structural typing interface for entities with integer ID."""

    id: int


@runtime_checkable
class NotifierProtocol(Protocol):
    """Structural interface for notifications."""

    def send_notification(self, recipient: str, message: str) -> str:
        ...


@runtime_checkable
class PaymentGateway(Protocol):
    """Structural interface for payment gateways."""

    def pay(self, amount: Money) -> str:
        ...


class DiscountPolicy(ABC):
    """Abstract Base Class for discount calculation."""

    @abstractmethod
    def apply(self, total: Money) -> Money:
        pass