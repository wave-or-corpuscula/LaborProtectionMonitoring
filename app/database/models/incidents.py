from peewee import *
from . import BaseModel, Employees


class Incidents(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='Сотрудники', verbose_name="Сотрудник", on_delete="cascade", on_update="cascade")
    incident_date = DateField(verbose_name="Дата инцидента", null=False)
    description = TextField(verbose_name="Описание", null=False)

    class Meta:
        table_name = "Инциденты"