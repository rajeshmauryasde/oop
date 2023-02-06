class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = [
    Employee("Rajesh", 200000),
    Employee("Mahesh", 10000),
    Employee("Mukesh", 50000),
    Employee("Gudiya", 150000)
]

for e in employees:
    print(f"{e.name}, {e.salary}")
