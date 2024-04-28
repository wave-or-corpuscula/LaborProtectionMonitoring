from peewee import *
from . import BaseModel


class SafetyBriefings(BaseModel):
    id = AutoField(primary_key=True)
    briefing_name = CharField(verbose_name="Инструктаж", null=False)
    description = TextField(verbose_name="Описание", null=False)
    date = DateField(verbose_name="Дата проведения", null=False)

    class Meta:
        table_name = "safety_briefings"