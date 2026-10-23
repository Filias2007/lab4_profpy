from typing import NotRequired, TypedDict


class ProductPayload(TypedDict):
    """DTO for external JSON-like product payload."""

    id: int
    name: str
    price: float
    category: str
    currency: NotRequired[str]