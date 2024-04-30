from peewee import *
from . import BaseModel, Departments, Employees


class EmployeesInDepartments(BaseModel):
    id = AutoField(primary_key=True)
    department_id = ForeignKeyField(Departments, backref='Департаменты', verbose_name="Департамент", on_delete="cascade", on_update="cascade")
    employee_id = ForeignKeyField(Employees, backref='Сотрудники', verbose_name="Сотрудник", on_delete="cascade", on_update="cascade")
    start_date = DateField(verbose_name="Дата начала работы", null=None)

    class Meta:
        table_name = "Сотрудники в департаменте"