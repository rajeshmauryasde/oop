from employee import Developer, Deployer
from report import JobTitleReport, SalaryReport

employees = [
    Developer("Rajesh", "Kumar", 200000),
    Deployer("Mahesh", "Kumar", 10000),
    Deployer("Mukesh", "Kumar", 50000),
    Developer("Gudiya", "Kumari", 150000),
]

reports = [
    JobTitleReport(employees=employees),
    SalaryReport(employees=employees),
]
for r in reports:
    r.print_report()
    print()
