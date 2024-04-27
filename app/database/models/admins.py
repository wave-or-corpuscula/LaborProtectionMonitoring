from peewee import *
from . import BaseModel, Users


class Admins(BaseModel):
    id = AutoField(primary_key=True)
    admin_user_id = ForeignKeyField(Users, backref='admin', verbose_name="Администраторы")

    class Meta:
        table_name = "admins"