from .base_model import BaseModel, db
from .departments import Departments
from .employees import Employees
from .employees_in_departments import EmployeesInDepartments
from .prefessions import Professions
from .employees_professions import EmployeesProfessions
from .incidents import Incidents
from .safety_briefings import SafetyBriefings
from .briefed_employees import BriefedEmployees
from .users import Users
from .admins import Admins


# tables_names = db.get_tables()

models = [
    Employees, 
    Departments, 
    Professions, 
    EmployeesInDepartments, 
    EmployeesProfessions, 
    Incidents, 
    SafetyBriefings, 
    BriefedEmployees, 
    Users, 
    Admins
]

def db_init():
    for table in models:
        if not db.table_exists(table):
            table.create_table()

get_model = {
    model._meta.table_name: model for model in models
}
