from peewee import *
from . import BaseModel


class SafetyBriefings(BaseModel):
    id = AutoField(primary_key=True)
    briefing_name = CharField()
    description = TextField()
    date = DateField()