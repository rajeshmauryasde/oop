from typing import List
from employee import Deployer, Developer


class Report:
    def __init__(self, employees: List) -> None:
        self._employees = employees


class SalaryReport(Report):
    def print_report(self) -> None:
        print(f"Accounting Report")
        print(f"=================")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.salary}")


class JobTitleReport(Report):
    def print_report(self) -> None:
        print(f"Employee Report")
        print(f"===============")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.job_title}")


class ScheduleReport(Report):
    def print_report(self) -> None:
        print(f"Schedule Report")
        print(f"===============")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.shift.get_shift_details()}")
