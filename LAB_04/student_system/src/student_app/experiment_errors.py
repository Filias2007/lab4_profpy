from student_app.models import Student
from student_app.repositories import InMemoryRepository

# Error 1: Wrong type assignment (str instead of int for id)
student_id: int = "1001"  # type: ignore (intended error)

# Error 2: Incompatible return type in function definition
def get_total_count() -> int:
    return "Not a number"  # type: ignore (intended error)

# Error 3: Generic type bound violation
repo: InMemoryRepository[Student] = InMemoryRepository()
repo.add("Not a Student Object")  # type: ignore (intended error)