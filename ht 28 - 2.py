class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_department(self):
        print(f"Department: {self.department}")

manager = Manager("kannu", 75000, "IT")
manager.display_details()
manager.display_department()
