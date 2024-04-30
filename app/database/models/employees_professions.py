from peewee import *
from . import BaseModel, Employees, Professions


class EmployeesProfessions(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='Сотрудники', verbose_name="Сотрудник", on_delete="cascade", on_update="cascade")
    profession_id = ForeignKeyField(Professions, backref='Профессии', verbose_name="Должность", on_delete="cascade", on_update="cascade")
    start_date = DateField(verbose_name="Дата начала работы", null=False)

    class Meta:
        table_name = "Профессии сотрудников"