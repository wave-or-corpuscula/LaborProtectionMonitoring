from peewee import *
from . import BaseModel, Employees, Professions


class EmployeesProfessions(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='professions', verbose_name="Работник")
    profession_id = ForeignKeyField(Professions, backref='employees', verbose_name="Должность")
    start_date = DateField(verbose_name="Дата начала работы")

    class Meta:
        table_name = "employees_professions"