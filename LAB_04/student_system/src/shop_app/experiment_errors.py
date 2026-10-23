from shop_app.models import Product
from shop_app.repositories import InMemoryRepository
from shop_app.value_objects import Money

# ==============================================================================
# Обов'язковий експеримент зі статичним аналізом типів (Mypy / Pyright)
# Файл містить 3 навмисні помилки типів для фіксації діагностики в звіті.
# ==============================================================================

# Error 1: Присвоєння неправильного типу (строка замість числа int для ID)
product_id: int = "1001"  # type: ignore[assignment]


# Error 2: Несумісний тип повертаного значення функції (строка замість Money)
def calculate_discounted_price(price: Money) -> Money:
    return "100.00 UAH"  # type: ignore[return-value]


# Error 3: Порушення обмеження TypeVar в Generic-репозиторії (передача строки замість Product)
repository: InMemoryRepository[Product] = InMemoryRepository()
repository.add("Not a Product Object")  # type: ignore[arg-type]