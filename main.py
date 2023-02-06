class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title


employees = [
    Employee("Rajesh", 200000, "SDE"),
    Employee("Mahesh", 10000, "DEVOPS"),
    Employee("Mukesh", 50000, "DEVOPS"),
    Employee("Gudiya", 150000, "SDE"),
]

for e in employees:
    print(f"{e.name}, {e.salary}, {e.job_title}")
