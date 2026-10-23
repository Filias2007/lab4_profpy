from abc import ABC, abstractmethod
from shop_app.dto import ProductPayload
from shop_app.models import Cart, Product
from shop_app.protocols import DiscountPolicy, NotifierProtocol, PaymentGateway
from shop_app.repositories import InMemoryRepository
from shop_app.value_objects import Money


# Inheritance example: Base class for notifications
class BaseNotificationService(ABC):
    def __init__(self, sender_name: str) -> None:
        self.sender_name = sender_name

    @abstractmethod
    def log_dispatch(self, recipient: str) -> None:
        pass


class EmailNotifier(BaseNotificationService):
    def log_dispatch(self, recipient: str) -> None:
        print(f"[{self.sender_name}] Dispatching notification to {recipient}")

    def send_notification(self, recipient: str, message: str) -> str:
        self.log_dispatch(recipient)
        print(f"Email sent to {recipient}: {message}")
        return f"MSG-{hash(message) % 10000:04d}"


class PercentageDiscount(DiscountPolicy):
    def __init__(self, percent: float) -> None:
        if not (0 <= percent <= 100):
            raise ValueError("Invalid discount percentage")
        self.percent = percent

    def apply(self, total: Money) -> Money:
        discounted = total.amount * (1 - self.percent / 100)
        return Money(discounted, total.currency)


class DemoPaymentGateway:
    def pay(self, amount: Money) -> str:
        print(f"Payment processed successfully: {amount}")
        return "PAY-SUCCESS-2026"


class StoreCatalogService:
    """Application Service orchestrating store operations with DI."""

    def __init__(
        self,
        repository: InMemoryRepository[Product],
        notifier: NotifierProtocol,
        payment_gateway: PaymentGateway,
        discount_policy: DiscountPolicy,
    ) -> None:
        self._repository = repository
        self._notifier = notifier
        self._payment_gateway = payment_gateway
        self._discount_policy = discount_policy

    def create_product_from_payload(self, payload: ProductPayload) -> Product:
        currency = payload.get("currency", "UAH")
        product = Product(
            id=payload["id"],
            name=payload["name"],
            category=payload["category"],
            _price=Money(payload["price"], currency),
        )
        self._repository.add(product)
        return product

    def get_most_expensive_product(self) -> Product | None:
        products = self._repository.get_all()
        if not products:
            return None
        return max(products, key=lambda p: p.price.amount)

    def checkout(self, customer_email: str, cart: Cart) -> Money:
        if len(cart) == 0:
            raise ValueError("Cart is empty")

        original_total = cart.total
        final_total = self._discount_policy.apply(original_total)
        payment_id = self._payment_gateway.pay(final_total)

        self._notifier.send_notification(
            recipient=customer_email,
            message=f"Order paid ({final_total}). Payment ID: {payment_id}",
        )
        return final_total