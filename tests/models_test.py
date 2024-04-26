from peewee import *

db = SqliteDatabase("tests/employees.sqlite", pragmas={'foreign_keys': 1})


class BaseModel(Model):

    class Meta:
        database = db


class Departments(BaseModel):
    department_name = CharField(verbose_name="Департамент", null=False)

    class Meta:
        table_name = "Departments_Tbl"


class Posts(BaseModel):
    post_name = CharField(verbose_name="Должность", null=False)

    class Meta:
        table_name = "Posts_Tbl"


class Employees(BaseModel):
    name = CharField(verbose_name="ФИО")
    department = ForeignKeyField(Departments, to_field=Departments.department_name, on_delete="SET NULL")
    post = ForeignKeyField(Posts, to_field=Posts.post_name, on_delete="SET NULL")
    hiring_date = DateField(verbose_name="Дата найма")
    last_briefing_date = DateField(verbose_name="Последний инструктаж")

    class Meta:
        table_name = "Employees_Tbl"


class Users(BaseModel):
    user_name = CharField(verbose_name="Имя пользователя", null=False)
    password = CharField(verbose_name="Пароль", null=False)

    class Meta:
        table_name = "Users_Tbl"

class Admins(BaseModel):
    admin_user = ForeignKeyField(Users, to_field=Users.user_name, on_delete="cascade")

    class Meta:
        table_name = "Admins_Tbl"

Departments.create_table()
Posts.create_table()
Employees.create_table()

Users.create_table()
Admins.create_table()


db.commit()
db.close()
