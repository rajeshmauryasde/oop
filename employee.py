class Employee:
    def __init__(self, first_name, last_name, salary, start_time, end_time):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
        self.start_time = start_time
        self.end_time = end_time

    def get_full_name(self):
        return f"{self._first_name}, {self._last_name}"


class Developer(Employee):
    job_title = "SDE"


class Deployer(Employee):
    job_title = "DEVOPS"
