from student_app.dto import StudentPayload
from student_app.models import AcademicRecord, Group, Student
from student_app.repositories import InMemoryRepository
from student_app.value_objects import Grade
from abc import ABC, abstractmethod
from student_app.protocols import NotifierProtocol, ReportingService

# Inheritance example: Base class for notifications
class BaseNotificationService(ABC):
    def __init__(self, sender_name: str) -> None:
        self.sender_name = sender_name

    @abstractmethod
    def log_dispatch(self, recipient: str) -> None:
        pass


class EmailNotifier(BaseNotificationService):
    """Concrete implementation matching NotifierProtocol via duck typing & inheritance."""

    def log_dispatch(self, recipient: str) -> None:
        print(f"[{self.sender_name}] Logged email delivery to {recipient}")

    def send_notification(self, recipient: str, message: str) -> str:
        self.log_dispatch(recipient)
        print(f"Email sent to {recipient}: {message}")
        return f"MSG-EMAIL-{hash(message) % 10000:04d}"


class TextSummaryReporter(ReportingService):
    """Concrete reporting service implementation."""

    def generate_report(self, students: list[Student]) -> str:
        lines = ["=== ACADEMIC PERFORMANCE REPORT ==="]
        for s in students:
            lines.append(f" - {s.full_name} (Group: {s.group_code}): GPA = {s.gpa:.2f}")
        return "\n".join(lines)


class StudentRegistryService:
    """Application Service orchestrating use cases using Dependency Injection."""

    def __init__(
        self,
        repository: InMemoryRepository[Student],
        notifier: NotifierProtocol,
        reporter: ReportingService,
    ) -> None:
        self._repository = repository
        self._notifier = notifier
        self._reporter = reporter

    def register_student_from_payload(self, payload: StudentPayload) -> Student:
        student = Student(
            id=payload["id"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            group_code=payload["group_code"],
        )
        if "initial_grades" in payload:
            rec = AcademicRecord(subject_name="General Intro")
            for val in payload["initial_grades"]:
                rec.add_grade(Grade(value=val))
            student.add_record(rec)

        self._repository.add(student)
        self._notifier.send_notification(
            recipient=f"{student.first_name.lower()}@university.edu.ua",
            message=f"Welcome {student.full_name}! Registration completed.",
        )
        return student

    def search_by_last_name(self, last_name: str) -> list[Student]:
        return [
            s for s in self._repository.get_all()
            if s.last_name.lower() == last_name.lower()
        ]
    def get_top_student(self) -> Student | None:
        all_students = self._repository.get_all()
        if not all_students:
            return None
        return max(all_students, key=lambda s: s.gpa)

    def generate_summary(self) -> str:
        return self._reporter.generate_report(self._repository.get_all())