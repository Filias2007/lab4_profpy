from student_app.dto import StudentPayload
from student_app.models import AcademicRecord, Group, Student
from student_app.repositories import InMemoryRepository
from student_app.services import EmailNotifier, StudentRegistryService, TextSummaryReporter
from student_app.value_objects import Grade


def main() -> None:
    print("--- 1. Initializing Repositories & Services (DI) ---")
    student_repo: InMemoryRepository[Student] = InMemoryRepository()
    email_notifier = EmailNotifier(sender_name="LNU Deanery Office")
    summary_reporter = TextSummaryReporter()

    registry_service = StudentRegistryService(
        repository=student_repo,
        notifier=email_notifier,
        reporter=summary_reporter,
    )

    print("\n--- 2. Registering Students from DTOs (TypedDict) ---")
    payload_1: StudentPayload = {
        "id": 1,
        "first_name": "Maksym",
        "last_name": "Filias",
        "group_code": "FEI-31",
        "initial_grades": [95.0, 88.5, 92.0],
    }
    payload_2: StudentPayload = {
        "id": 2,
        "first_name": "Khrystyna",
        "last_name": "Tomchenko",
        "group_code": "FEI-31",
        "initial_grades": [98.0, 96.0, 100.0],
    }

    s1 = registry_service.register_student_from_payload(payload_1)
    s2 = registry_service.register_student_from_payload(payload_2)

    print("\n--- 3. Adding More Academic Records ---")
    ds_record = AcademicRecord(subject_name="Data Structures")
    ds_record.add_grade(Grade(value=90.0, weight=1.0))
    ds_record.add_grade(Grade(value=85.0, weight=0.8))
    s1.add_record(ds_record)

    print("\n--- 4. Group Container Operations (Dunder methods) ---")
    group = Group(code="FEI-31", faculty="Electronics & Computer Technologies")
    group.add_student(s1)
    group.add_student(s2)

    print(f"Group count (len): {len(group)}")
    print(f"Is Student #1 in group? {1 in group}")
    print(f"Direct Indexing group[2]: {group[2].full_name}")

    print("\nIteration over Group:")
    for student in group:
        print(f"  -> {student}")

    print("\n--- 5. Business Logic: Search & Best Student ---")
    search_results = registry_service.search_by_last_name("Filias")
    print(f"Search 'Filias' found: {[s.full_name for s in search_results]}")

    best_student = registry_service.get_top_student()
    if best_student:
        print(f"Best Performing Student: {best_student.full_name} with GPA = {best_student.gpa:.2f}")

    print("\n--- 6. Reporting Service Output ---")
    report = registry_service.generate_summary()
    print(report)


if __name__ == "__main__":
    main()