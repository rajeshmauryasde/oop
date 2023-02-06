class Employee:
    def __init__(self, first_name, last_name, salary):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self._first_name}, {self._last_name}"


class Developer(Employee):
    job_title = "SDE"


class Maintainer(Employee):
    job_title = "DEVOPS"
