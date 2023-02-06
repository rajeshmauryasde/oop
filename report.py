
class SalaryReport:
    def __init__(self, employees):
        self._employees = employees

    def print_salary_report(self):
        print(f"====Salary Report====")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.salary}")


class JobTitleReport:
    def __init__(self, employees):
        self._employees = employees

    def print_job_title_report(self):
        print(f"====Job Title Report====")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.job_title}")
