import datetime

from .models import *
from .db_methods import *



def test():
    data = get_employees_last_briefed()
        
    for row in data:
        print(row)