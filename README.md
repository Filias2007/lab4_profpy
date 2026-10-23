# Online Store System (Lab 4 - Variant 3)

Навчально-демонстраційний проєкт із професійного ООП та суворої системи типів Python у межах Лабораторної роботи №4 (Варіант 3 — Система управління та обліку інтернет-магазину).

## Особливості реалізації

- **Domain Model & Encapsulation**: Сутності `Product`, `Cart`, `CartItem` з інкапсуляцією та властивостями (`@property` з валідацією).
- **Value Objects**: Immutable клас `Money` (`frozen=True`, `slots=True`) з перевіркою від'ємних сум, збігу валют та арифметичними dunder-методами.
- **Abstractions & Protocols**:
  - `ABC`: `DiscountPolicy`, `BaseNotificationService`.
  - `Protocol` (Structural Typing): `NotifierProtocol`, `PaymentGateway`, `EntityWithId`.
- **Generic Repository**: Універсальний репозиторій `InMemoryRepository[T]` із обмеженням типів через `TypeVar("T", bound=EntityWithId)`.
- **DTO**: Опис зовнішніх JSON-пакетів товарів через `TypedDict` (`ProductPayload`).
- **SOLID & Dependency Injection**: Повний прокид залежностей у `StoreCatalogService` без жорсткої прив'язки до конкретних класів інфраструктури.

## Структура проєкту

```text
student_system/
├── pyproject.toml
├── README.md
└── src/
    └── shop_app/
        ├── __init__.py
        ├── dto.py
        ├── experiment_errors.py
        ├── models.py
        ├── protocols.py
        ├── repositories.py
        ├── services.py
        ├── value_objects.py
        └── main.py