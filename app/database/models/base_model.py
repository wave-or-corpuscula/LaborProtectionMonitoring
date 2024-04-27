from peewee import *

db = SqliteDatabase('app/database/database.sqlite')

class BaseModel(Model):
    class Meta:
        database = db