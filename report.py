from typing import List
from employee import Employee


class Report:
    def __init__(self, employees: List[Employee]):
        self._employees = employees


class SalaryReport(Report):
    def print_report(self):
        print(f"Accounting Report")
        print(f"=================")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.salary}")


class JobTitleReport(Report):
    def print_report(self):
        print(f"Employee Report")
        print(f"===============")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.job_title}")


class ScheduleReport(Report):
    def print_report(self):
        print(f"Schedule Report")
        print(f"===============")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.start_time:%H:%m} to {e.end_time:%H:%m}")
