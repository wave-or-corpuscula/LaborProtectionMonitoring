from peewee import *
from . import BaseModel


class Employees(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(verbose_name="ФИО", null=False)
    hiring_date = DateField(verbose_name="Дата найма", null=False)
    phone = CharField(verbose_name="Номер телефона", null=False)
    is_male = BooleanField(verbose_name="Пол", null=False)

    class Meta:
        table_name = "Сотрудники"