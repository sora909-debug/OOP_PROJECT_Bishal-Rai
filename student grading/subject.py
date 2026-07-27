class Subject:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = float(marks)

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def get_grade(self):
        if self.__marks >= 90:
            return "A+"
        elif self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B+"
        elif self.__marks >= 60:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "F"

    def display(self):
        print(f"{self.__name} : {self.__marks} ({self.get_grade()})")