"""Online Store System package (Lab 4 - Variant 3)."""

from shop_app.dto import ProductPayload
from shop_app.models import Cart, CartItem, Product
from shop_app.protocols import DiscountPolicy, EntityWithId, NotifierProtocol, PaymentGateway
from shop_app.repositories import InMemoryRepository
from shop_app.services import BaseNotificationService, DemoPaymentGateway, EmailNotifier, PercentageDiscount, StoreCatalogService
from shop_app.value_objects import Money

__all__ = [
    "Money",
    "ProductPayload",
    "Product",
    "CartItem",
    "Cart",
    "EntityWithId",
    "NotifierProtocol",
    "PaymentGateway",
    "DiscountPolicy",
    "BaseNotificationService",
    "InMemoryRepository",
    "EmailNotifier",
    "PercentageDiscount",
    "DemoPaymentGateway",
    "StoreCatalogService",
]