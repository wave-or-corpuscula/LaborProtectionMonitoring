from peewee import *
from . import BaseModel, Employees, Professions


class EmployeesProfessions(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='employees', verbose_name="Сотрудник", on_delete="cascade", on_update="cascade")
    profession_id = ForeignKeyField(Professions, backref='professions', verbose_name="Должность", on_delete="cascade", on_update="cascade")
    start_date = DateField(verbose_name="Дата начала работы")

    class Meta:
        table_name = "employees_professions"