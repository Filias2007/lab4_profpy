"""Corrected version of experiment code for clean Mypy status."""

from shop_app.models import Product
from shop_app.repositories import InMemoryRepository
from shop_app.value_objects import Money

# Fix 1: Correct int type
product_id: int = 1001

# Fix 2: Correct Money return type
def calculate_discounted_price(price: Money) -> Money:
    return Money(price.amount * 0.9, price.currency)

# Fix 3: Correct Product object passed to repository
repository: InMemoryRepository[Product] = InMemoryRepository()
repository.add(
    Product(
        id=1,
        name="Laptop",
        category="Electronics",
        _price=Money(1000.0),
    )
)