from peewee import *
from . import BaseModel


class Professions(BaseModel):
    id = AutoField(primary_key=True)
    profession_name = CharField()