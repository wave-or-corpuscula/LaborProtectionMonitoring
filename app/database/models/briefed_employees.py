from peewee import *
from . import BaseModel, Employees, SafetyBriefings


class BriefedEmployees(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='Сотрудники', verbose_name="Сотрудник", on_delete="cascade", on_update="cascade")
    briefing_id = ForeignKeyField(SafetyBriefings, backref='Инструктажи', verbose_name="Инструктаж", on_delete="cascade", on_update="cascade")

    class Meta:
        table_name = "Инструктажи сотрудиков"