from PySide6.QtCore import Slot
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QMainWindow

from .BriefingsUi import Ui_BriefingsWindow
from app.utils import TableManager
from app.database import SafetyBriefings
from app.database.db_methods import get_employees_last_briefed, select_all, get_verbose_columns
from app.signals import *


class BriefingsForm(QMainWindow):

    def __init__(self, 
                 parent=None, 
                 menu_signals: MenuSignals = None, 
                 briefing_signals: BriefingsSignals = None):
        super(BriefingsForm, self).__init__(parent)
        self.ui = Ui_BriefingsWindow()
        self.ui.setupUi(self)

        self.employees_columns = ["id работника", "Работник", "Последний инструктаж", "Дата", "Следующий инструктаж"]
        self.empl_tmanager = TableManager(self.ui.employees_tw, hidden_cols=[0])
        self.briefings_columns = get_verbose_columns(SafetyBriefings._meta.table_name)
        self.brief_tmanager = TableManager(self.ui.briefings_tw, hidden_cols=[0])
        
        empl_data = get_employees_last_briefed()
        self.empl_tmanager.fill_table(empl_data, self.employees_columns)
        inst_data = select_all(SafetyBriefings)
        self.brief_tmanager.fill_table(inst_data, self.briefings_columns)

        # Cursom signals connection

        self.menu_signals = menu_signals
        self.briefing_signals = briefing_signals

        self.menu_signals.goto_briefing.connect(self.show)

        # Generic signals connection

        self.ui.back_pb.clicked.connect(self.goto_menu)



        # self.employees_set_tables_info()

    @Slot()
    def goto_menu(self):
        self.hide()
        self.briefing_signals.goto_menu.emit()

    def showEvent(self, event: QShowEvent) -> None:
        self.employees_set_tables_info()

    def employees_set_tables_info(self):
        empl_data = get_employees_last_briefed()
        self.empl_tmanager.fill_table(empl_data)
        inst_data = select_all(SafetyBriefings)
        self.brief_tmanager.fill_table(inst_data)
        

    def departments_set_tables_info(self):
        pass