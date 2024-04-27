from peewee import *

db = SqliteDatabase('app/database/database.sqlite', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db