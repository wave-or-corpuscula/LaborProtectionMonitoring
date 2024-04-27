from .models import *
from .db_methods import *

def test():
    for row in select_all(Admins):
        print(row)