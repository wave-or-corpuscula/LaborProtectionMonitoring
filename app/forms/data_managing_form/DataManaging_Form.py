from peewee import *

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QLineEdit, QHBoxLayout, QDateEdit, QComboBox

from .DataManagingUi import Ui_DataManagingWindow
from app.database import *
from app.database.db_methods import *
from app.utils import TableManager
from app.signals import MenuSignals, DataManagingSignals


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
        self.ui.dataDisplay_tw.itemClicked.connect(self.item_selected)

        # Other stuff setup 

        self.foreign_keys_ids = {}

        self.tables = [self.get_model_name(model) for model in models]
        self.ui.currentTable_cb.addItems([table for table in self.tables])

    @Slot()
    def item_selected(self, item: QTableWidgetItem):
        for i in range(self.ui.dataDisplay_tw.columnCount()):
            print(self.ui.dataDisplay_tw.item(item.row(), i).text())

    @staticmethod
    def get_model_name(model: BaseModel):
        return model._meta.table_name

    def get_table_columns(self, table: str):
        model = get_model[table]
        columns = db.get_columns(table)
        verbose_columns = [model._meta.fields[col.name].verbose_name if model._meta.fields[col.name].verbose_name else col.name for col in columns]
        self.columns_types = {v_col: col_type for v_col, col_type in zip(verbose_columns, model._meta.fields.values())}
        return verbose_columns

    @Slot()
    def show_current_table(self):
        cur_table = self.tables[self.ui.currentTable_cb.currentIndex()]
        columns = self.get_table_columns(cur_table)
        data = select_all(get_model[cur_table])
        self.tmanager.fill_table(data=data, columns=columns)
        self.set_table_inputs()
    
    def set_table_inputs(self):
        self.foreign_keys_ids.clear()
        self.clear_layout(self.ui.inputs_hbl)
        for col_name, col_type in self.columns_types.items():
            if isinstance(col_type, CharField) or isinstance(col_type, TextField):
                inp = QLineEdit()
                inp.setPlaceholderText(col_name)
                self.ui.inputs_hbl.addWidget(inp)
            elif isinstance(col_type, DateField):
                inp = QDateEdit()
                self.ui.inputs_hbl.addWidget(inp)
            elif isinstance(col_type, BooleanField):
                inp = QComboBox()
                inp.addItems(["М", "Ж"])
                self.ui.inputs_hbl.addWidget(inp)
            elif isinstance(col_type, ForeignKeyField):
                inp = QComboBox()
                inp.setObjectName(col_name)
                first_col_dict = {data[1]: data[0] for data in select_all(get_model[col_type.backref])}
                self.foreign_keys_ids[col_name] = first_col_dict
                inp.addItems(first_col_dict.keys())
                self.ui.inputs_hbl.addWidget(inp)
        print(self.foreign_keys_ids)

    @Slot()
    def goto_menu(self):
        self.data_manage_signals.goto_menu.emit()
        self.hide()
    
    @Slot()
    def user_enters(self):
        self.show()

    @staticmethod
    def clear_layout(layout: QHBoxLayout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()
            # layout.removeItem(layout.itemAt(i))
