from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from .DataManagingUi import Ui_DataManagingWindow
from app.signals import MenuSignals, DataManagingSignals
from app.database import *
from app.utils import TableManager

class DataManagingForm(QMainWindow):

    def __init__(self, 
                 parent=None, 
                 menu_signals: MenuSignals = None, 
                 data_manage_signals: DataManagingSignals = None):
        super(DataManagingForm, self).__init__(parent)
        self.ui = Ui_DataManagingWindow()
        self.ui.setupUi(self)

        self.tmanager = TableManager(self.ui.dataDisplay_tw)

        # Custom signals connection

        self.data_manage_signals = data_manage_signals

        self.menu_signals = menu_signals
        self.menu_signals.goto_data_change.connect(self.user_enters)

        # Generic signals connection

        self.ui.backToMenu_pb.clicked.connect(self.goto_menu)
        self.ui.currentTable_cb.currentIndexChanged.connect(self.show_current_table)

        # Other stuff setup 

        self.tables = Users._meta.database.get_tables()
        self.ui.currentTable_cb.addItems([table for table in self.tables])


    def get_table_columns(self, table: str):
        model = get_model[table]
        columns = db.get_columns(table)
        verbose_columns = [model._meta.fields[col.name].verbose_name if model._meta.fields[col.name].verbose_name else col.name for col in columns]
        print(verbose_columns)

    @Slot()
    def show_current_table(self):
        cur_table = self.tables[self.ui.currentTable_cb.currentIndex()]
        columns = self.get_table_columns(cur_table)

    @Slot()
    def goto_menu(self):
        self.data_manage_signals.goto_menu.emit()
        self.hide()
    
    @Slot()
    def user_enters(self):
        self.show()
