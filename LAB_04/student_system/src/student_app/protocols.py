from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from student_app.models import Student


class EntityWithId(Protocol):
    """Structural interface ensuring domain entity has an integer ID."""

    id: int


@runtime_checkable
class NotifierProtocol(Protocol):
    """Structural interface for notification services."""

    def send_notification(self, recipient: str, message: str) -> str:
        ...


class ReportingService(ABC):
    """Abstract Base Class (ABC) for generating academic reports."""

    @abstractmethod
    def generate_report(self, students: list[Student]) -> str:
        pass