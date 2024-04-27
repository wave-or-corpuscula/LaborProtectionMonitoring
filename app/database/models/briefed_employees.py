from peewee import *
from . import BaseModel, Employees, SafetyBriefings


class BriefedEmployees(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='employees', verbose_name="Сотрудник")
    briefing_id = ForeignKeyField(SafetyBriefings, backref='safety_briefings', verbose_name="Инструктаж")

    class Meta:
        table_name = "briefed_employees"