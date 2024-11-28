class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def show_student_id(self):
        print(f"Student ID: {self.student_id}")

student = Student("knnu", "e24ai018")
student.show_name()
student.show_student_id()
