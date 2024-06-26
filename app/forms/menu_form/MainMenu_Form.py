from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from .MainMenuUi import Ui_MenuWindow
from app.utils import User
from app.signals import *


class MenuForm(QMainWindow):

    def __init__(self, 
                 parent=None, 
                 auth_signals: AuthorizationSignals = None, 
                 menu_signals: MenuSignals = None,
                 data_manage_signals: DataManagingSignals = None,
                 briefing_signals: BriefingsSignals = None):
        super(MenuForm, self).__init__(parent)
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

        self.user = None

        # Custom signals connection

        self.auth_signals = auth_signals
        self.auth_signals.user_authorized.connect(self.update_user_info)

        self.menu_signals = menu_signals

        self.data_manage_signals = data_manage_signals
        self.data_manage_signals.goto_menu.connect(self.user_back)

        self.briefing_signals = briefing_signals
        self.briefing_signals.goto_menu.connect(self.user_back)

        # Signals connection

        self.ui.logout_pb.clicked.connect(self.logout)
        self.ui.changeData_pb.clicked.connect(self.goto_data_change)
        self.ui.briefingCheck_pb.clicked.connect(self.goto_briefings)
        self.ui.exit_pb.clicked.connect(self.close)

    def goto_briefings(self):
        self.hide()
        self.menu_signals.goto_briefing.emit(self.user)

    @Slot()
    def user_back(self):
        self.show()

    @Slot()
    def goto_data_change(self):
        self.hide()
        self.menu_signals.goto_data_change.emit(self.user)

    @Slot(User)
    def update_user_info(self, user: User):
        self.user = user
        self.ui.username_lb.setText(user.username)
        if user.is_admin:
            self.ui.username_lb.setStyleSheet("border: 1px solid yellow")
        else:
            self.ui.username_lb.setStyleSheet("border: 1px solid black")
        self.user = user
        self.show()

    @Slot()
    def logout(self):
        self.hide()
        self.menu_signals.user_logout.emit()