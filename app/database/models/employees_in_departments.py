from peewee import *
from . import BaseModel, Departments, Employees


class EmployeesInDepartments(BaseModel):
    id = AutoField(primary_key=True)
    department_id = ForeignKeyField(Departments, backref='employees')
    employee_id = ForeignKeyField(Employees, backref='departments')
    start_date = DateField()