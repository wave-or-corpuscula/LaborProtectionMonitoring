from peewee import *
from . import BaseModel


class Users(BaseModel):
    id = AutoField(primary_key=True)
    username = CharField(unique=True, verbose_name="Имя пользователя")
    password = CharField(verbose_name="Пароль")


    class Meta:
        table_name = "users"