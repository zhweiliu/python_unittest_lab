from my_project.models.student import Student


def find_student_by_id(id: int) -> Student:
    # query database
    return Student(1, 'Andy')


def save_student(student: Student):
    # update database
    pass


def change_name(student_id: int, name: str):
    student = find_student_by_id(student_id)

    if student is not None:
        student.name = name
        save_student(student)
