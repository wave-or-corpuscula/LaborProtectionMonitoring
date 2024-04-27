from peewee import *
from . import BaseModel, Users


class Admins(BaseModel):
    id = AutoField(primary_key=True)
    admin_user = ForeignKeyField(Users, backref='admin')