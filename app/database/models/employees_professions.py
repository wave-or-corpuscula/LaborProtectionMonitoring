from peewee import *
from . import BaseModel, Employees, Professions


class EmployeesProfessions(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='professions')
    profession_id = ForeignKeyField(Professions, backref='employees')
    start_date = DateField()