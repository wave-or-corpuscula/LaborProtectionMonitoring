import sys

from PySide6.QtWidgets import QApplication

from app.forms import *
from app.signals import *
from app.database import db_init


class FormsController:

    def __init__(self):
        self.app = QApplication(sys.argv)

        # Custom signals
        auth_signals = AuthorizationSignals()
        menu_signals = MenuSignals()
        data_manage_signals = DataManagingSignals()

        # Forms
        self.authorization_form = AuthorizationForm(auth_signals=auth_signals, menu_signals=menu_signals)
        self.menu_form = MenuForm(auth_signals=auth_signals, menu_signals=menu_signals, data_manage_signals=data_manage_signals)
        self.data_managing_form = DataManagingForm(menu_signals=menu_signals, data_manage_signals=data_manage_signals)

    def run_app(self):
        db_init()
        window = self.data_managing_form
        window.show()
        sys.exit(self.app.exec())
