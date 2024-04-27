from models import *


Employees._meta.database.connect()
Employees._meta.database.create_tables([Employees, 
                                        Departments, 
                                        EmployeesInDepartments, 
                                        Professions, 
                                        EmployeesProfessions, 
                                        Incidents, 
                                        SafetyBriefings,
                                        BriefedEmployees,
                                        Users,
                                        Admins])