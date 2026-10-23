from dataclasses import dataclass, field
from typing import Iterator
from shop_app.value_objects import Money


@dataclass
class Product:
    """Domain object representing a Product."""

    id: int
    name: str
    category: str
    _price: Money

    @property
    def price(self) -> Money:
        return self._price

    @price.setter
    def price(self, new_price: Money) -> None:
        if new_price.amount < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    def __str__(self) -> str:
        return f"Product #{self.id}: {self.name} ({self.price}) [{self.category}]"

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, category={self.category!r})"


@dataclass
class CartItem:
    """Domain object representing item in a shopping cart."""

    product: Product
    quantity: int = 1

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")

    @property
    def total(self) -> Money:
        return Money(
            amount=self.product.price.amount * self.quantity,
            currency=self.product.price.currency,
        )


class Cart:
    """Container class representing a shopping cart (Custom Collection)."""

    def __init__(self) -> None:
        self._items: list[CartItem] = []

    def add(self, product: Product, quantity: int = 1) -> None:
        self._items.append(CartItem(product=product, quantity=quantity))

    @property
    def total(self) -> Money:
        if not self._items:
            return Money(0.0)
        total_amount = sum(item.total.amount for item in self._items)
        return Money(total_amount, self._items[0].product.price.currency)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[CartItem]:
        return iter(self._items)

    def __contains__(self, product_id: int) -> bool:
        return any(item.product.id == product_id for item in self._items)

    def __getitem__(self, index: int) -> CartItem:
        return self._items[index]