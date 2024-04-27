from peewee import *
from . import BaseModel


class Departments(BaseModel):
    id = AutoField(primary_key=True)
    department_name = CharField(verbose_name="Департамент")

    class Meta:
        table_name = "departments"