from peewee import *

db = SqliteDatabase("app/database/employees.sqlite", pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class Departments(BaseModel):
    id = AutoField(primary_key=True)
    department_name = CharField(verbose_name="Департаменты", null=False)


class Posts(BaseModel):
    id = AutoField(primary_key=True)
    post_name = CharField(verbose_name="Должности", null=False)


class Employees(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(verbose_name="ФИО")
    department_id = ForeignKeyField(Departments, backref='employees', null=True, on_delete='SET NULL', verbose_name="Департамент")
    post_id = ForeignKeyField(Posts, backref='employees', null=True, on_delete='SET NULL', verbose_name="Должность")
    hiring_date = DateField(verbose_name="Дата найма")
    last_briefing_date = DateField(verbose_name="Последний инструктаж")


class Users(BaseModel):
    id = AutoField(primary_key=True)
    user_name = CharField(verbose_name="Имя пользователя", null=False)
    password = CharField(verbose_name="Пароль", null=False)

    def __str__(self):
        return f"<id:{self.id},username:{self.user_name},pass:{self.password}>"


class Admins(BaseModel):
    id = AutoField(primary_key=True)
    admin_user_id = ForeignKeyField(Users, backref='admins', null=True, on_delete='CASCADE', verbose_name="Админы")


get_model = {
    "departments": Departments,
    "posts": Posts,
    "employees": Employees,
    "users": Users,
    "admins": Admins,
}


def check_user(username: str, password: str):
    try:
        user = Users.get(Users.user_name == username, Users.password == password)
        # Проверяем, является ли пользователь администратором
        try:
            admin = Admins.get(Admins.admin_user_id == user.id)
            is_admin = True
        except Admins.DoesNotExist:
            is_admin = False
        return user, is_admin
    except Users.DoesNotExist:
        return None, False


def db_init():
    tables = [Departments, Posts, Employees, Users, Admins]
    for table in tables:
        if not db.table_exists(table):
            table.create_table()
            