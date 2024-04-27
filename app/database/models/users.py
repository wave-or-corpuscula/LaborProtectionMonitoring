from peewee import *
from . import BaseModel


class Users(BaseModel):
    id = AutoField(primary_key=True)
    username = CharField(unique=True)
    password = CharField()