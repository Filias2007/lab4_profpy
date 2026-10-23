from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True, slots=True)
class Grade:
    """Immutable Value Object representing an academic grade (0 to 100)."""

    value: float
    weight: float = 1.0

    def __post_init__(self) -> None:
        if not (0.0 <= self.value <= 100.0):
            raise ValueError(f"Grade value must be between 0 and 100, got: {self.value}")
        if not (0.0 < self.weight <= 1.0):
            raise ValueError(f"Grade weight must be in (0, 1], got: {self.weight}")

    @property
    def weighted_value(self) -> float:
        return self.value * self.weight

    def __str__(self) -> str:
        return f"{self.value:.1f} (w={self.weight:.2f})"

    def __add__(self, other: object) -> float:
        if isinstance(other, Grade):
            return self.value + other.value
        if isinstance(other, (int, float)):
            return self.value + float(other)
        return NotImplemented

    def __radd__(self, other: float) -> float:
        return self.value + other