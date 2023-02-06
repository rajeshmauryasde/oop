class Report:
    def __init__(self, employees):
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
