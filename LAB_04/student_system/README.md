# Student Management System (Lab 4)

Учебно-демонстрационный проект с профессиональным ООП и строгой системой типов Python в рамках Лабораторной работы №4 (Вариант 1 — Система учета студентов).

## Особенности реализации

- **Domain Model**: Сущности `Student`, `Group`, `AcademicRecord` с инкапсуляцией и свойствами (`@property`).
- **Value Objects**: Immutable класс `Grade` (`frozen=True`, `slots=True`) с валидацией диапазона оценок (0..100) и перегрузкой операторов.
- **Abstractions & Protocols**:
  - `ABC`: `BaseNotificationService`, `ReportingService`.
  - `Protocol` (Structural Typing): `NotifierProtocol`, `EntityWithId`.
- **Generic Repository**: Универсальный репозиторий `InMemoryRepository[T]` с ограничением типов через `TypeVar("T", bound=EntityWithId)`.
- **DTO**: Описание внешних payloads через `TypedDict` (`StudentPayload`).
- **SOLID & Dependency Injection**: Полный прокид зависимостей в `StudentRegistryService` без жесткой привязки к конкретным классам.

## Структура проекта

```text
student_system/
├── pyproject.toml
├── README.md
└── src/
    └── student_app/
        ├── __init__.py
        ├── dto.py
        ├── models.py
        ├── protocols.py
        ├── repositories.py
        ├── services.py
        ├── value_objects.py
        └── main.py