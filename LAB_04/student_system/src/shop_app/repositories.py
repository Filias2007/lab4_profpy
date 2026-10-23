from typing import Generic, TypeVar
from shop_app.protocols import EntityWithId

T = TypeVar("T", bound=EntityWithId)


class InMemoryRepository(Generic[T]):
    """Generic repository implementation for entities with ID."""

    def __init__(self) -> None:
        self._storage: dict[int, T] = {}

    def add(self, item: T) -> None:
        self._storage[item.id] = item

    def get(self, item_id: int) -> T | None:
        return self._storage.get(item_id)

    def get_all(self) -> list[T]:
        return list(self._storage.values())

    def remove(self, item_id: int) -> bool:
        return self._storage.pop(item_id, None) is not None

    def __len__(self) -> int:
        return len(self._storage)