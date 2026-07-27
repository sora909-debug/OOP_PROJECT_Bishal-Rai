from person import Student
from subject import Subject


class GradingSystem:
    def __init__(self):
        self.__students = []

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.__students.append(student)
        print("Student added successfully!")

    def find_student(self, student_id):
        for student in self.__students:
            if student.get_id() == student_id:
                return student
        return None

    def add_subject(self, student_id, subject_name, marks):
        student = self.find_student(student_id)

        if student is None:
            print("Student not found.")
            return

        subject = Subject(subject_name, marks)
        student.add_subject(subject)

        print("Subject added successfully!")

    def view_students(self):
        if not self.__students:
            print("No students found.")
            return

        for student in self.__students:
            student.display()

            total = 0

            for subject in student.get_subjects():
                subject.display()
                total += subject.get_marks()

            if student.get_subjects():
                average = total / len(student.get_subjects())
                print(f"Average Marks: {average:.2f}")