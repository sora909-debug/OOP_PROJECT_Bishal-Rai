class Person:
    def __init__(self, person_id, name):
        self.__person_id = person_id
        self.__name = name

    def get_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name


class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.__subjects = []

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def get_subjects(self):
        return self.__subjects

    def display(self):
        print("\n----- Student -----")
        print(f"ID   : {self.get_id()}")
        print(f"Name : {self.get_name()}")