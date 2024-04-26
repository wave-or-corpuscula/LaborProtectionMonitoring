from datetime import date

from models import *

db_init()

def add_department(name):
    department = Departments.create(department_name=name)
    return department


def add_post(name):
    post = Posts.create(post_name=name)
    return post


def add_employee(name, department_id, post_id, hiring_date, briefing_date):
    employee = Employees.create(name=name, department_id=department_id, post_id=post_id, hiring_date=hiring_date, last_briefing_date=briefing_date)
    return employee


def add_user(user_name, password):
    user = Users.create(user_name=user_name, password=password)
    return user


def add_admin(user_id):
    admin = Admins.create(admin_user_id=user_id)
    return admin


RECORDS_AMOUNT = 10

users_data = [
    {"user_name": f"user{i}", "password": f"password{i}"} for i in range(1, RECORDS_AMOUNT + 1)
]

employees_data = [
    {"name": f"Employee {i}", "department_id": (i % 3) + 1, "post_id": (i % 3) + 1, "hiring_date": date(2020, 1, i % 28 + 1), "briefing_date": date(2022, 1, i % 28 + 1)} for i in range(1, RECORDS_AMOUNT + 1)
]

posts = ["Developer", "Manager", "Accountant"]

departments = ["IT", "HR", "Finance"]

def fill_db():
    for department in departments:
        add_department(department)
    for post in posts:
        add_post(post)
    for employee_data in employees_data:
        add_employee(**employee_data)
    for user_data in users_data:
        add_user(**user_data)
    for i in range(1, 3):
        add_admin(i)
    
fill_db()
    