from employee import Developer, Maintainer
from report import JobTitleReport, SalaryReport

employees = [
    Developer("Rajesh", "Kumar", 200000),
    Maintainer("Mahesh", "Kumar", 10000),
    Maintainer("Mukesh", "Kumar", 50000),
    Developer("Gudiya", "Kumari", 150000),
]

reports = [
    JobTitleReport(employees=employees),
    SalaryReport(employees=employees),
]
for r in reports:
    if type(r) is JobTitleReport:
        r.print_job_title_report()
    else:
        r.print_salary_report()
