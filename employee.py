from shift import MorningShift, AfternoonShift


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        salary: int,
        shift: MorningShift | AfternoonShift,
    ) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
        self.shift = shift

    def get_full_name(self) -> str:
        return f"{self._first_name}, {self._last_name}"


class Developer(Employee):
    job_title = "SDE"


class Deployer(Employee):
    job_title = "DEVOPS"
