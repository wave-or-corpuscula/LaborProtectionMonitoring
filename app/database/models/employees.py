from peewee import *
from . import BaseModel


class Employees(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(verbose_name="ФИО")
    hiring_date = DateField(verbose_name="Дата найма")
    phone = CharField(verbose_name="Номер телефона")
    is_male = BooleanField(verbose_name="Пол")

    class Meta:
        table_name = "employees"