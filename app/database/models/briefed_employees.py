from peewee import *
from . import BaseModel, Employees, SafetyBriefings


class BriefedEmployees(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='briefings', verbose_name="Сотрудник")
    briefing_id = ForeignKeyField(SafetyBriefings, backref='employees', verbose_name="Инструктаж")

    class Meta:
        table_name = "briefed_employees"