import datetime

from peewee import fn

from app.database import Employees, BriefedEmployees, SafetyBriefings, db

def get_employees_last_briefed():
    data = []
    all_employees_query = (BriefedEmployees
                           .select(BriefedEmployees.employee_id, Employees.name)
                           .join(SafetyBriefings, on=(BriefedEmployees.briefing_id == SafetyBriefings.id))
                           .switch(BriefedEmployees)
                           .join(Employees, on=(BriefedEmployees.employee_id == Employees.id))
                           .order_by(SafetyBriefings.date))
    all_employees = [row for row in db.execute_sql(str(all_employees_query))]
    return all_employees
    # for empl in all_employees:
    #     row = [empl.id, empl.name]
    #     query = (BriefedEmployees
    #                 .select(SafetyBriefings.briefing_name, fn.MAX(SafetyBriefings.date))
    #                 .where(BriefedEmployees.employee_id == empl.id)
    #                 .join(SafetyBriefings, on=(BriefedEmployees.briefing_id == SafetyBriefings.id))
    #         )
    #     for col in db.execute_sql(str(query)):
    #         row += col
    #     data.append(row)

    # for row_ind in range(len(data)):
    #     data_item = data[row_ind][-1]
    #     if data_item:
    #         last_brief_date = datetime.datetime.strptime(data_item, "%Y-%m-%d").date()
    #         next_brief_date = last_brief_date + datetime.timedelta(days=180)
    #         data[row_ind][-1] = last_brief_date
    #         data[row_ind].append(next_brief_date)
    #     else:
    #         data[row_ind][-2] = "Не проходил"
    #         data[row_ind][-1] = "Не проходил"
    #         data[row_ind].append("Не проходил")
    return data