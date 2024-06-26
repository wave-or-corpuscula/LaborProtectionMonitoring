import sys

import hashlib

from PySide6.QtWidgets import QApplication

from app.forms import *
from app.signals import *
from app.database import db_init


class FormsController:

    def __init__(self):
        self.app = QApplication(sys.argv)

        self.hash_func = lambda string : hashlib.md5(string.encode()).hexdigest()

        # Custom signals
        auth_signals = AuthorizationSignals()
        menu_signals = MenuSignals()
        data_manage_signals = DataManagingSignals()
        briefing_signals = BriefingsSignals()

        # Forms
        self.authorization_form = AuthorizationForm(auth_signals=auth_signals, menu_signals=menu_signals, hash_func=self.hash_func)
        self.menu_form = MenuForm(auth_signals=auth_signals, menu_signals=menu_signals, data_manage_signals=data_manage_signals, briefing_signals=briefing_signals)
        self.data_managing_form = DataManagingForm(menu_signals=menu_signals, data_manage_signals=data_manage_signals, hash_func=self.hash_func)
        self.briefings_form = BriefingsForm(menu_signals=menu_signals, briefing_signals=briefing_signals)

    def run_app(self):
        db_init()
        window = self.authorization_form
        window.show()
        sys.exit(self.app.exec())
