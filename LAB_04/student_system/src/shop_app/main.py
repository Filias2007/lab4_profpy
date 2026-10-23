from shop_app.dto import ProductPayload
from shop_app.models import Cart, Product
from shop_app.repositories import InMemoryRepository
from shop_app.services import DemoPaymentGateway, EmailNotifier, PercentageDiscount, StoreCatalogService


def main() -> None:
    print("--- 1. Initializing Store Infrastructure (DI) ---")
    product_repo: InMemoryRepository[Product] = InMemoryRepository()
    notifier = EmailNotifier(sender_name="Online Store Support")
    payment_gateway = DemoPaymentGateway()
    discount_policy = PercentageDiscount(percent=10.0)  # 10% discount

    store_service = StoreCatalogService(
        repository=product_repo,
        notifier=notifier,
        payment_gateway=payment_gateway,
        discount_policy=discount_policy,
    )

    print("\n--- 2. Registering Products from TypedDict DTOs ---")
    p1_payload: ProductPayload = {
        "id": 101,
        "name": "Gaming Laptop",
        "category": "Electronics",
        "price": 45000.0,
    }
    p2_payload: ProductPayload = {
        "id": 102,
        "name": "Wireless Mouse",
        "category": "Electronics",
        "price": 1500.0,
    }

    prod1 = store_service.create_product_from_payload(p1_payload)
    prod2 = store_service.create_product_from_payload(p2_payload)

    print(f"Registered: {prod1}")
    print(f"Registered: {prod2}")

    print("\n--- 3. Custom Container Cart Operations (Dunder methods) ---")
    cart = Cart()
    cart.add(prod1, quantity=1)
    cart.add(prod2, quantity=2)

    print(f"Cart item count (len): {len(cart)}")
    print(f"Product #101 in cart? {101 in cart}")
    print(f"Cart total before discount: {cart.total}")

    print("\n--- 4. Business Operations ---")
    most_expensive = store_service.get_most_expensive_product()
    if most_expensive:
        print(f"Most expensive product: {most_expensive.name} ({most_expensive.price})")

    print("\n--- 5. Checkout Process ---")
    final_paid = store_service.checkout("customer@example.com", cart)
    print(f"Final Paid Amount: {final_paid}")


if __name__ == "__main__":
    main()