from typing import NotRequired, TypedDict


class StudentPayload(TypedDict):
    """External payload DTO representation (JSON/API-like)."""

    id: int
    first_name: str
    last_name: str
    group_code: str
    initial_grades: NotRequired[list[float]]