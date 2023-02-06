from employee import Developer, Maintainer
from report import JobTitleReport, SalaryReport

employees = [
    Developer("Rajesh", "Kumar", 200000),
    Maintainer("Mahesh", "Kumar", 10000),
    Maintainer("Mukesh", "Kumar", 50000),
    Developer("Gudiya", "Kumari", 150000),
]

job_title_report = JobTitleReport(employees=employees)
job_title_report.print_job_title_report()
print()
salary_report = SalaryReport(employees=employees)
salary_report.print_salary_report()