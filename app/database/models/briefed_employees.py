from peewee import *
from . import BaseModel, Employees, SafetyBriefings


class BriefedEmployees(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='briefings')
    briefing_id = ForeignKeyField(SafetyBriefings, backref='employees')