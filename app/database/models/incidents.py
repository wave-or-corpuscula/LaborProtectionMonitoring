from peewee import *
from . import BaseModel, Employees


class Incidents(BaseModel):
    id = AutoField(primary_key=True)
    employee_id = ForeignKeyField(Employees, backref='incidents')
    incident_date = DateField()
    description = TextField()