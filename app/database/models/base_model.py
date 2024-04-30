from peewee import *

print("Hell0")
db = SqliteDatabase('./app/database/database.sqlite', pragmas={'foreign_keys': 1})
print("Db connected")

class BaseModel(Model):
    class Meta:
        database = db