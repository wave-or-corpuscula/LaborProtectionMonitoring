from peewee import *

from app.database.models import *


def add_record(model: BaseModel, data: dict):
    try:
        model.create(**data)
    except Exception as e:
        raise

def delete_record(model: BaseModel, record_id: int):
    try:
        model.delete_by_id(record_id)
    except Exception as e:
        print(f"record_id: {record_id}, Error: {e}")

def update_record(model: BaseModel, update_id: int, data: dict):
    try:
        model.update(**data).where(model.id == update_id).execute()
    except Exception as e:
        raise

def get_verbose_columns(table: str):
    model = get_model[table]
    columns = db.get_columns(table)
    verbose_columns = [model._meta.fields[col.name].verbose_name if model._meta.fields[col.name].verbose_name else col.name for col in columns]
    return verbose_columns

def select_all(model: BaseModel):
    table = model._meta.table_name
    match table:
        case BriefedEmployees._meta.table_name:
            query = """SELECT "t1"."id", "t2"."name", "t3"."briefing_name" 
FROM "briefed_employees" AS "t1" 
INNER JOIN "employees" AS "t2" ON ("t1"."employee_id" = "t2"."id") 
INNER JOIN "safety_briefings" AS "t3" ON ("t1"."briefing_id" = "t3"."id")"""
            return [row for row in db.execute_sql(query)]
        case EmployeesInDepartments._meta.table_name:
            query = """SELECT "t1"."id", "t2"."department_name", "t3"."name", "t1"."start_date" 
FROM "employees_in_departments" AS "t1" 
INNER JOIN "employees" AS "t3" ON ("t1"."department_id" = "t2"."id") 
INNER JOIN "departments" AS "t2" ON ("t1"."employee_id" = "t3"."id")"""
            return [row for row in db.execute_sql(query)]
        case EmployeesProfessions._meta.table_name:
            query = """SELECT "t1"."id", "t2"."name", "t3"."profession_name", "t1"."start_date" 
FROM "employees_professions" AS "t1" 
INNER JOIN "employees" AS "t2" ON ("t1"."employee_id" = "t2"."id") 
INNER JOIN "professions" AS "t3" ON ("t1"."profession_id" = "t3"."id")"""
            return [row for row in db.execute_sql(query)]
        case Incidents._meta.table_name:
            query = """SELECT "t1"."id", "t2"."name", "t1"."incident_date", "t1"."description" 
FROM "incidents" AS "t1" 
INNER JOIN "employees" AS "t2" ON ("t1"."employee_id" = "t2"."id")"""
            return [row for row in db.execute_sql(query)]
        case Admins._meta.table_name:
            query = """SELECT "t1"."id", "t2"."username" 
FROM "admins" AS "t1" 
INNER JOIN "users" AS "t2" ON ("t1"."admin_user_id" = "t2"."id")"""
            return [row for row in db.execute_sql(query)]
        case Employees._meta.table_name:
            query = """SELECT "t1"."id", "t1"."name", "t1"."hiring_date", "t1"."phone", 
CASE WHEN "t1"."is_male" THEN 'М' ELSE 'Ж' END 
FROM "employees" AS "t1" 
ORDER BY "t1"."id" """
            return [row for row in db.execute_sql(query)]
        case _:
            query = model.select()
    try:
        dict_data = [row.__dict__["__data__"] for row in query.execute()]
        return [list(row.values()) for row in dict_data]
    except Exception as e:
        print(f"Error: {e}")