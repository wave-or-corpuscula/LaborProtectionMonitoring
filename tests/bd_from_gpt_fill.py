from datetime import date

from bd_from_gpt import *

# Заполнение таблиц данными
departments_data = [
    {"department_name": "IT"},
    {"department_name": "HR"},
    {"department_name": "Finance"},
]

posts_data = [
    {"post_name": "Developer"},
    {"post_name": "Manager"},
    {"post_name": "Accountant"},
]

users_data = [
    {"user_name": "user1", "password": "password1"},
    {"user_name": "user2", "password": "password2"},
]

# Заполнение таблиц данными
DepartmentsTbl.insert_many(departments_data).execute()
PostsTbl.insert_many(posts_data).execute()
UsersTbl.insert_many(users_data).execute()

# Получаем ID добавленных записей
department_ids = {department.department_name: department.id for department in DepartmentsTbl.select()}
post_ids = {post.post_name: post.id for post in PostsTbl.select()}
user_ids = {user.user_name: user.id for user in UsersTbl.select()}

employees_data = [
    {"name": "Иванов Иван Иванович", "department_id": department_ids["IT"], "post_id": post_ids["Developer"], "hiring_date": date(2020, 1, 1), "last_briefing_date": date(2022, 1, 1)},
    {"name": "Петров Петр Петрович", "department_id": department_ids["HR"], "post_id": post_ids["Manager"], "hiring_date": date(2019, 5, 15), "last_briefing_date": date(2021, 5, 15)},
    {"name": "Сидоров Сидор Сидорович", "department_id": department_ids["Finance"], "post_id": post_ids["Accountant"], "hiring_date": date(2021, 3, 10), "last_briefing_date": date(2023, 3, 10)},
]

admins_data = [
    {"admin_user_id": user_ids["user1"]},
]

# Заполнение таблиц данными
AdminsTbl.insert_many(admins_data).execute()
EmployeesTbl.insert_many(employees_data).execute()