"""Student Management System package (Lab 4)."""

from student_app.dto import StudentPayload
from student_app.models import AcademicRecord, Group, Student
from student_app.protocols import EntityWithId, NotifierProtocol, ReportingService
from student_app.repositories import InMemoryRepository
from student_app.services import BaseNotificationService, EmailNotifier, StudentRegistryService, TextSummaryReporter
from student_app.value_objects import Grade

__all__ = [
    "Grade",
    "StudentPayload",
    "AcademicRecord",
    "Student",
    "Group",
    "EntityWithId",
    "NotifierProtocol",
    "ReportingService",
    "BaseNotificationService",
    "InMemoryRepository",
    "EmailNotifier",
    "TextSummaryReporter",
    "StudentRegistryService",
]