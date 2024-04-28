from peewee import *
from . import BaseModel


class Users(BaseModel):
    id = AutoField(primary_key=True)
    username = CharField(unique=True, verbose_name="Имя пользователя", null=False)
    password = CharField(verbose_name="Пароль", null=False)


    class Meta:
        table_name = "users"