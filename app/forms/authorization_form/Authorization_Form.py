from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox

from .AuthorizationUi import Ui_AuthorizationWindow
from app.database.db_methods import check_user
from app.signals import AuthorizationSignals, MenuSignals

from app.utils import User


class AuthorizationForm(QMainWindow):

    def __init__(self, 
                 parent=None, 
                 auth_signals: AuthorizationSignals = None, 
                 menu_signals: MenuSignals = None,
                 hash_func = None):
        super(AuthorizationForm, self).__init__(parent)
        self.ui = Ui_AuthorizationWindow()
        self.ui.setupUi(self)

        self.hash_func = hash_func

        self.auth_signals = auth_signals
        self.menu_signals = menu_signals

        self.menu_signals.user_logout.connect(self.user_logout)

        self.ui.signIn_pb.clicked.connect(self.authorize)

    @Slot()
    def user_logout(self):
        self.show()

    @Slot()
    def authorize(self):
        username = self.ui.username_le.text()
        password = self.ui.password_le.text()

        user, is_admin = check_user(username, self.hash_func(password))
        if not user:
            QMessageBox.about(self, "Ошибка", "Пользователя не существует!")
        else:
            self.hide()
            self.auth_signals.user_authorized.emit(User(username, is_admin))
        self.ui.username_le.clear()
        self.ui.password_le.clear()