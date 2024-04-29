import datetime

from peewee import fn

from app.database import Employees, BriefedEmployees, SafetyBriefings, db

def get_employees_last_briefed():
    query = (BriefedEmployees
             .select(Employees.name, SafetyBriefings.briefing_name, fn.MAX(SafetyBriefings.date))
             .join(Employees, on=(BriefedEmployees.employee_id == Employees.id))
             .switch(BriefedEmployees)
             .join(SafetyBriefings, on=(BriefedEmployees.briefing_id == SafetyBriefings.id))
             .group_by(Employees.name)
             .order_by(fn.MAX(SafetyBriefings.date))
             )
    data = [[c for c in row] for row in db.execute_sql(str(query))]
    for row_ind in range(len(data)):
        last_brief_date = datetime.datetime.strptime(data[row_ind][-1], "%Y-%m-%d").date()
        next_brief_date = last_brief_date + datetime.timedelta(days=180)
        data[row_ind][-1] = last_brief_date
        data[row_ind].append(next_brief_date)
    return data