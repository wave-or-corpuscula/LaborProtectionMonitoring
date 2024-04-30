from datetime import date

import hashlib

from models import *

db_init()


with db.atomic():
    # # Заполнение таблицы Employees
    # for i in range(1, 6):
    #     Employees.create(name=f'Employee_{i}', hiring_date=date.today(), phone=f'123-456-789{i}', is_male=True)

    # # Заполнение таблицы Departments
    # for i in range(1, 6):
    #     Departments.create(department_name=f'Department_{i}')

    # # Заполнение таблицы EmployeesInDepartment
    # for i in range(1, 6):
    #     EmployeesInDepartments.create(department_id=i, employee_id=i, start_date=date.today())

    # # Заполнение таблицы Professions
    # for i in range(1, 6):
    #     Professions.create(profession_name=f'Profession_{i}')

    # # Заполнение таблицы EmployeesProfessions
    # for i in range(1, 6):
    #     EmployeesProfessions.create(employee_id=i, profession_id=i, start_date=date.today())

    # # Заполнение таблицы Incidents
    # for i in range(1, 6):
    #     Incidents.create(employee_id=i, incident_date=date.today(), description=f'Incident_{i}')

    # # Заполнение таблицы SafetyBriefings
    # for i in range(1, 6):
    #     SafetyBriefings.create(briefing_name=f'Briefing_{i}', description=f'Description_{i}', date=date.today())

    # # Заполнение таблицы BriefedEmployees
    # for i in range(1, 6):
    #     BriefedEmployees.create(employee_id=i, briefing_id=i)

    # # Заполнение таблицы Users
    # for i in range(1, 6):
    #     Users.create(username=f'user_{i}', password=f'password_{i}')

    # # Заполнение таблицы Admins
    # for i in range(1, 2):
    #     Admins.create(admin_user_id=i)
    Users.create(username='admin', password=hashlib.md5('admin'.encode()).hexdigest())
    Admins.create(admin_user_id=1)