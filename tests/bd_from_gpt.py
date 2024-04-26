from peewee import *

db = SqliteDatabase("tests/employees.sqlite", pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class DepartmentsTbl(BaseModel):
    id = AutoField(primary_key=True)
    department_name = CharField(null=False)


class PostsTbl(BaseModel):
    id = AutoField(primary_key=True)
    post_name = CharField(null=False)


class EmployeesTbl(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    department_id = ForeignKeyField(DepartmentsTbl, backref='employees', null=True, on_delete='SET NULL')
    post_id = ForeignKeyField(PostsTbl, backref='employees', null=True, on_delete='SET NULL')
    hiring_date = DateField()
    last_briefing_date = DateField()


class UsersTbl(BaseModel):
    id = AutoField(primary_key=True)
    user_name = CharField(null=False)
    password = CharField(null=False)


class AdminsTbl(BaseModel):
    id = AutoField(primary_key=True)
    admin_user_id = ForeignKeyField(UsersTbl, backref='admins', null=True, on_delete='CASCADE')


# Создание таблиц
db.connect()
# db.create_tables([DepartmentsTbl, PostsTbl, EmployeesTbl, UsersTbl, AdminsTbl])
print(db.table_exists(DepartmentsTbl))