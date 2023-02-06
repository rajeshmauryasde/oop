class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
    job_title = "SDE"


class Maintainer(Employee):
    job_title = "DEVOPS"


employees = [
    Developer("Rajesh", 200000),
    Maintainer("Mahesh", 10000),
    Maintainer("Mukesh", 50000),
    Developer("Gudiya", 150000),
]

for e in employees:
    print(f"{e.name}, {e.salary}, {e.job_title}")
