from peewee import *
from . import BaseModel, Departments, Employees


class EmployeesInDepartments(BaseModel):
    id = AutoField(primary_key=True)
    department_id = ForeignKeyField(Departments, backref='departments', verbose_name="Департамент")
    employee_id = ForeignKeyField(Employees, backref='employees', verbose_name="Сотрудник")
    start_date = DateField(verbose_name="Дата начала работы")

    class Meta:
        table_name = "employees_in_departments"