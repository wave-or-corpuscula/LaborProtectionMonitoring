import datetime

from PySide6.QtGui import QColor
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from .BriefingsUi import Ui_BriefingsWindow
from app.utils import TableManager, User
from app.database import SafetyBriefings, BriefedEmployees
from app.database.db_methods import get_employees_last_briefed, select_all, get_verbose_columns, add_record
from app.signals import *


class BriefingsForm(QMainWindow):

    def __init__(self, 
                 parent=None, 
                 menu_signals: MenuSignals = None, 
                 briefing_signals: BriefingsSignals = None):
        super(BriefingsForm, self).__init__(parent)
        self.ui = Ui_BriefingsWindow()
        self.ui.setupUi(self)
        
        self.user = None

        self.selected_employee_id = None
        self.selected_briefing_id = None

        self.employees_columns = ["id", "Работник", "Последний инструктаж", "Дата", "Следующий инструктаж"]
        self.empl_tmanager = TableManager(self.ui.employees_tw, hidden_cols=[0])
        self.briefings_columns = get_verbose_columns(SafetyBriefings._meta.table_name)
        self.brief_tmanager = TableManager(self.ui.briefings_tw, hidden_cols=[0])

        # Employees search input
        self.ui.employeesSearch_le.textEdited.connect(self.search_employees)

        # Briefings date filter 
        self.ui.filterBriefings_pb.clicked.connect(self.date_filter_briefings)
        self.ui.cancelFilterBriefings_pb.clicked.connect(self.cancel_date_filter)
        
        self.empl_data = get_employees_last_briefed()
        self.empl_tmanager.fill_table(self.empl_data, self.employees_columns)
        self.inst_data = select_all(SafetyBriefings)
        self.brief_tmanager.fill_table(self.inst_data, self.briefings_columns)

        # Cursom signals connection

        self.menu_signals = menu_signals
        self.briefing_signals = briefing_signals

        self.menu_signals.goto_briefing.connect(self.user_enter)

        # Generic signals connection

        self.ui.back_pb.clicked.connect(self.goto_menu)
        self.ui.instruct_pb.clicked.connect(self.instruct_employee)
        self.ui.employees_tw.itemClicked.connect(self.select_employee)
        self.ui.briefings_tw.itemClicked.connect(self.select_briefing)

    def cancel_date_filter(self):
        self.brief_tmanager.fill_table(self.inst_data)

    def date_filter_briefings(self):
        start_date = self.ui.briefingsStart_de.date()
        end_date = self.ui.briefingEnd_de.date()

        self.brief_tmanager.fill_with_date_filter(self.inst_data, start_date, end_date, 3)

    def search_employees(self, filter_text: str):
        self.empl_tmanager.fill_with_filter(self.empl_data, filter_text.lower())
        self.color_expired_briefings()

    def select_briefing(self, item: QTableWidgetItem):
        self.selected_briefing_id = self.ui.briefings_tw.item(item.row(), 0).text()
        self.ui.selectedBriefing_le.setText(self.ui.briefings_tw.item(item.row(), 1).text())

    def select_employee(self, item: QTableWidgetItem):
        self.selected_employee_id = self.ui.employees_tw.item(item.row(), 0).text()
        self.ui.selectedEmployee_le.setText(self.ui.employees_tw.item(item.row(), 1).text())

    def instruct_employee(self):
        if not self.user.is_admin:
            QMessageBox.critical(self, "Недостаточно прав", "Только администратор может инструктировать сотрудников!")
            return
        if not self.selected_employee_id:
            QMessageBox.warning(self, "Не выбран работник", "Сначала выребете работника!")
            return
        if not self.selected_briefing_id:
            QMessageBox.warning(self, "Не выбран инструктаж", "Сначала выребете инструктаж!")
            return
        add_record(BriefedEmployees, {"briefing_id": self.selected_briefing_id, 
                                      "employee_id": self.selected_employee_id})
        self.employees_set_tables_info()

    @Slot(User)
    def user_enter(self, user: User):
        self.user = user
        self.show()

    @Slot()
    def goto_menu(self):
        self.hide()
        self.briefing_signals.goto_menu.emit()

    def color_expired_briefings(self):
        for row in range(self.ui.employees_tw.rowCount()):
            if self.ui.employees_tw.item(row, 2).text() == "Не проходил":
                for col in range(len(self.employees_columns)):
                    item = self.ui.employees_tw.item(row, col)
                    item.setBackground(QColor("red"))
                continue
            next_brief_date = datetime.datetime.strptime(self.ui.employees_tw.item(row, 4).text(), "%Y-%m-%d").date()
            if (next_brief_date - datetime.datetime.today().date()).total_seconds() < 0:
                for col in range(len(self.employees_columns)):
                    item = self.ui.employees_tw.item(row, col)
                    item.setBackground(QColor("red"))
                continue

    def showEvent(self, event) -> None:
        self.employees_set_tables_info()
        self.ui.selectedBriefing_le.setText("Не выбран")
        self.ui.selectedEmployee_le.setText("Не выбран")
        self.selected_briefing_id = None
        self.selected_employee_id = None

    def employees_set_tables_info(self):
        self.empl_data = get_employees_last_briefed()
        self.empl_tmanager.fill_table(self.empl_data)
        self.inst_data = select_all(SafetyBriefings)
        self.brief_tmanager.fill_table(self.inst_data)
        self.color_expired_briefings()
