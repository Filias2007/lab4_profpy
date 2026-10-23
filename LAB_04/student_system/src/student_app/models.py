from dataclasses import dataclass, field
from typing import Iterator
from student_app.value_objects import Grade


@dataclass
class AcademicRecord:
    """Domain object holding student's list of grades."""

    subject_name: str
    grades: list[Grade] = field(default_factory=list)

    def add_grade(self, grade: Grade) -> None:
        self.grades.append(grade)

    @property
    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        total_weighted = sum(g.weighted_value for g in self.grades)
        total_weights = sum(g.weight for g in self.grades)
        return total_weighted / total_weights if total_weights > 0 else 0.0

    def __len__(self) -> int:
        return len(self.grades)


@dataclass
class Student:
    """Domain object representing a Student."""

    id: int
    first_name: str
    last_name: str
    group_code: str
    _records: list[AcademicRecord] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def add_record(self, record: AcademicRecord) -> None:
        self._records.append(record)

    @property
    def gpa(self) -> float:
        if not self._records:
            return 0.0
        valid_averages = [r.average_grade for r in self._records if len(r) > 0]
        if not valid_averages:
            return 0.0
        return sum(valid_averages) / len(valid_averages)

    def __str__(self) -> str:
        return f"Student #{self.id}: {self.full_name} [{self.group_code}] - GPA: {self.gpa:.2f}"

    def __repr__(self) -> str:
        return f"Student(id={self.id!r}, name={self.full_name!r}, group={self.group_code!r})"


class Group:
    """Domain collection class with custom container behavior."""

    def __init__(self, code: str, faculty: str) -> None:
        self.code = code
        self.faculty = faculty
        self._students: dict[int, Student] = {}

    def add_student(self, student: Student) -> None:
        self._students[student.id] = student

    def remove_student(self, student_id: int) -> bool:
        return self._students.pop(student_id, None) is not None

    def __len__(self) -> int:
        return len(self._students)

    def __iter__(self) -> Iterator[Student]:
        return iter(self._students.values())

    def __contains__(self, student_id: int) -> bool:
        return student_id in self._students

    def __getitem__(self, student_id: int) -> Student:
        if student_id not in self._students:
            raise KeyError(f"Student ID {student_id} not found in group {self.code}")
        return self._students[student_id]