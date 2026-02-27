class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def new_salary(self, new_salary):
        self.salary = new_salary+self.salary*20
        print(f"New salary after 20% increase: {self.salary}")


    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
emp1 = Employee("Alice", 30, 50000)
emp1.display_info()
emp1.new_salary(5000)