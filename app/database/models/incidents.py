from peewee import *
from . import BaseModel, Employees


class Incidents(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='incidents', verbose_name="Сотрудник")
    incident_date = DateField(verbose_name="Дата инцидента")
    description = TextField(verbose_name="Описание")

    class Meta:
        table_name = "incidents"