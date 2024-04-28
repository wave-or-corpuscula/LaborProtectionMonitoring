from peewee import *
from . import BaseModel, Users


class Admins(BaseModel):
    id = AutoField(primary_key=True)
    admin_user_id = ForeignKeyField(Users, backref='users', verbose_name="Администраторы", on_delete="cascade", on_update="cascade")

    class Meta:
        table_name = "admins"