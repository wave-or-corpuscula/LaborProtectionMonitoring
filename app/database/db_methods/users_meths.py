from app.database.models import Users, Admins


def check_user(username: str, password: str):
    try:
        user = Users.get(Users.username == username, Users.password == password)
        # Проверяем, является ли пользователь администратором
        try:
            admin = Admins.get(Admins.admin_user_id == user.id)
            is_admin = True
        except Admins.DoesNotExist:
            is_admin = False
        return user, is_admin
    except Users.DoesNotExist:
        return None, False