from datetime import date

from models_test import *

# Создаем таблицы
# db.create_tables([Departments, Posts, Employees, Users, Admins])

# Заполнение таблиц

departments_data = [
    {"department_name": "IT"},
    {"department_name": "HR"},
    {"department_name": "Finance"},
]

for data in departments_data:
    Departments.create(**data)

posts_data = [
    {"post_name": "Developer"},
    {"post_name": "Manager"},
    {"post_name": "Accountant"},
]

for data in posts_data:
    Posts.create(**data)

employees_data = [
    {"name": "Иванов Иван Иванович", "post": "Developer", "department": "IT", "hiring_date": date(2020, 1, 1), "last_briefing_date": date(2022, 1, 1)},
    {"name": "Петров Петр Петрович", "post": "Manager", "department": "HR", "hiring_date": date(2019, 5, 15), "last_briefing_date": date(2021, 5, 15)},
    {"name": "Сидоров Сидор Сидорович", "post": "Accountant", "department": "Finance", "hiring_date": date(2021, 3, 10), "last_briefing_date": date(2023, 3, 10)},
]

for data in employees_data:
    print(Employees.insert_many(data))

users_data = [
    {"user_name": "user1", "password": "password1"},
    {"user_name": "user2", "password": "password2"},
]

for data in users_data:
    Users.create(**data)

admins_data = [
    {"admin_user": "user1"},
]

for data in admins_data:
    Admins.create(**data)
