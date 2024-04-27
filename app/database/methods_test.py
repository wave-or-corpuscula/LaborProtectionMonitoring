from .models import *
from .db_methods import *

def test():
    for user in select_all(Employees):
        print(user.name, user.hiring_date, user.phone, user.is_male)
    # update_record(Users, 1, username="user1", password="password1")
    # add_record(Users, username="user_1", password="password_1")
    # delete_record(Users, 10)