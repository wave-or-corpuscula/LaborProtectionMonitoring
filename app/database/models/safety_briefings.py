from peewee import *
from . import BaseModel


class SafetyBriefings(BaseModel):
    id = AutoField(primary_key=True)
    briefing_name = CharField(verbose_name="Инструктаж")
    description = TextField(verbose_name="Описание")
    date = DateField(verbose_name="Дата проведения")

    class Meta:
        table_name = "safety_briefings"