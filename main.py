from shift import MorningShift, AfternoonShift
from employee import Developer, Deployer
from report import JobTitleReport, SalaryReport, ScheduleReport

employees = [
    Developer("Rajesh", "Kumar", 200000, MorningShift()),
    Deployer("Mahesh", "Kumar", 10000, MorningShift()),
    Deployer("Mukesh", "Kumar", 50000, AfternoonShift()),
    Developer("Gudiya", "Kumari", 150000, AfternoonShift()),
]

reports = [
    JobTitleReport(employees=employees),
    SalaryReport(employees=employees),
    ScheduleReport(employees=employees),
]
for r in reports:
    r.print_report()
    print()
