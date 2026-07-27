from grading import GradingSystem


def menu():
    grading = GradingSystem()

    while True:
        print("\n" + "=" * 40)
        print("        STUDENT GRADING SYSTEM")
        print("=" * 40)
        print("1. Add Student")
        print("2. Add Subject Marks")
        print("3. View Student Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Student ID: ")
            name = input("Student Name: ")
            grading.add_student(student_id, name)

        elif choice == "2":
            student_id = input("Student ID: ")
            subject = input("Subject Name: ")
            marks = input("Marks: ")
            grading.add_subject(student_id, subject, marks)

        elif choice == "3":
            grading.view_students()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()