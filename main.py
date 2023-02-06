import datetime
from employee import Developer, Deployer
from report import JobTitleReport, SalaryReport, ScheduleReport

employees = [
    Developer("Rajesh", "Kumar", 200000, datetime.time(9, 00), datetime.time(18, 00)),
    Deployer("Mahesh", "Kumar", 10000, datetime.time(9, 00), datetime.time(18, 00)),
    Deployer("Mukesh", "Kumar", 50000, datetime.time(14, 00), datetime.time(22, 00)),
    Developer("Gudiya", "Kumari", 150000, datetime.time(14, 00), datetime.time(22, 00)),
]

reports = [
    JobTitleReport(employees=employees),
    SalaryReport(employees=employees),
    ScheduleReport(employees=employees),
]
for r in reports:
    r.print_report()
    print()
