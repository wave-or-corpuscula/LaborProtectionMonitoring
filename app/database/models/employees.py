from peewee import *
from . import BaseModel


class Employees(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    hiring_date = DateField()
    phone = CharField()
    is_male = BooleanField()