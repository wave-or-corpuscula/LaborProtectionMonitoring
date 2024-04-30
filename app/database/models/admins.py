from peewee import *
from . import BaseModel, Users


class Admins(BaseModel):
    id = AutoField(primary_key=True)
    admin_user_id = ForeignKeyField(Users, backref='Пользователи', verbose_name="Администраторы", on_delete="cascade", on_update="cascade", unique=True)

    class Meta:
        table_name = "Администраторы"