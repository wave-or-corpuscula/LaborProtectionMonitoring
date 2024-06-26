from peewee import *

from PySide6.QtCore import Slot, QDate
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QLineEdit, QHBoxLayout, QDateEdit, QComboBox, QMessageBox

from .DataManagingUi import Ui_DataManagingWindow
from app.database import *
from app.database.db_methods import *
from app.utils import TableManager, User
from app.signals import MenuSignals, DataManagingSignals


class DataManagingForm(QMainWindow):

    def __init__(self, 
                 parent=None, 
                 menu_signals: MenuSignals = None, 
                 data_manage_signals: DataManagingSignals = None,
                 hash_func = None):
        super(DataManagingForm, self).__init__(parent)
        self.ui = Ui_DataManagingWindow()
        self.ui.setupUi(self)

        self.user = None
        self.hash_func = hash_func

        self.tmanager = TableManager(self.ui.dataDisplay_tw, hidden_cols=[0])

        # Custom signals connection

        self.data_manage_signals = data_manage_signals

        self.menu_signals = menu_signals
        self.menu_signals.goto_data_change.connect(self.user_enters)

        # Generic signals connection

        self.ui.backToMenu_pb.clicked.connect(self.goto_menu)
        self.ui.currentTable_cb.currentIndexChanged.connect(self.show_current_table)
        self.ui.dataDisplay_tw.itemClicked.connect(self.item_selected)
        self.ui.deleteRecord_pb.clicked.connect(self.del_record)
        self.ui.addRecord_pb.clicked.connect(self.add_record)
        self.ui.changeRecord_pb.clicked.connect(self.change_record)

        # Other stuff setup 

        self.record_id = None
        self.foreign_keys_ids = {}

        self.tables = [self.get_model_name(model) for model in models]
        self.ui.currentTable_cb.addItems([table for table in self.tables])

    @property
    def getInputDict(self):
        columns = [col.name for col in db.get_columns(self.curTable)[1:]]
        values = self.get_inputs_data()
        if self.curTable == Users._meta.table_name:
            values[-1] = self.hash_func(values[-1])
        return {col: val for col, val in zip(columns, values)}

    @Slot()
    def change_record(self):
        if self.curTable == Admins._meta.table_name:
            if not self.user.is_admin:
                QMessageBox.critical(self, "Недостаточно прав", "Вы не можете изменить администратора!")
                return
        if self.curTable == Users._meta.table_name:
            if not self.user.is_admin and check_admin(int(self.record_id)):
                QMessageBox.critical(self, "Недостаточно прав", "Пользователь является администратором, вы не можете его изменить!")
                return
        if self.record_id:
            try:
                update_record(self.curModel, self.record_id, self.getInputDict)
                self.refresh_data()
            except Exception as e:
                if "NOT NULL" in str(e):
                    QMessageBox.critical(self, "Некорректные данные", "Все поля должны быть заполнены!")
                else:
                    QMessageBox.critical(self, "Некорректные данные", "Ошибка при изменении данных")
        else:
            QMessageBox.warning(self, "Запись не выбрана", "Перед изменением выберете запись!")

    @Slot()
    def add_record(self):
        if self.curTable == Admins._meta.table_name:
            if not self.user.is_admin:
                QMessageBox.critical(self, "Недостаточно прав", "Вы не можете добавить администратора!")
                return
        try:
            add_record(self.curModel, self.getInputDict)
            self.refresh_data()
        except Exception as e:
            if "NOT NULL" in str(e):
                QMessageBox.critical(self, "Некорректные данные", "Все поля должны быть заполнены!")
            elif "UNIQUE" in str(e):
                QMessageBox.critical(self, "Некорректные данные", "Записи должны быть уникальны!")
            else:
                QMessageBox.critical(self, "Ошибка при добавлении данных", str(e))

    def get_inputs_data(self):
        data = []
        for i in range(self.ui.inputs_hbl.count()):
            widget = self.ui.inputs_hbl.itemAt(i).widget()
            if isinstance(widget, QLineEdit):
                append_data = widget.text() if widget.text() else None
                data.append(append_data)
            elif isinstance(widget, QDateEdit):
                data.append(widget.date().toString(u"yyyy-MM-dd"))
            elif isinstance(widget, QComboBox):
                obj_name = widget.objectName()
                if obj_name == "is_male":
                    data.append(widget.currentText() == "М")
                else:
                    f_key_id = self.foreign_keys_ids[obj_name][widget.currentText()]
                    data.append(f_key_id)
        return data

    @Slot()
    def del_record(self):
        if self.curTable == Admins._meta.table_name:
            if not self.user.is_admin:
                QMessageBox.critical(self, "Недостаточно прав", "Вы не можете удалить администратора!")
                return
        if self.curTable == Users._meta.table_name or self.curTable == Admins._meta.table_name:
            if get_username(self.record_id) == self.user.username:
                QMessageBox.critical(self, "Ошибка", "Вы не можете удалить себя!")
                return
            elif not self.user.is_admin and check_admin(int(self.record_id)):
                QMessageBox.critical(self, "Недостаточно прав", "Пользователь является администратором, вы не можете его удалить!")
                return
        if self.record_id:
            delete_record(self.curModel, self.record_id)
            self.refresh_data()
            self.record_id = None
        else:
            QMessageBox.warning(self, "Запись не выбрана", "Перед удалением выберете запись!")

    @Slot()
    def item_selected(self, item: QTableWidgetItem):
        row_data = self.get_row_data(item.row())
        self.record_id = row_data[0]
        row_data_no_id = row_data[1:]
        for i, item_val in zip(range(self.ui.inputs_hbl.count()), row_data_no_id):
            widget = self.ui.inputs_hbl.itemAt(i).widget()
            if isinstance(widget, QLineEdit):
                widget.setText(item_val)
            elif isinstance(widget, QDateEdit):
                widget.setDate(QDate.fromString(item_val, u"yyyy-MM-dd"))
            elif isinstance(widget, QComboBox):
                widget.setCurrentText(item_val)

    def get_row_data(self, row_num: int):
        return [self.ui.dataDisplay_tw.item(row_num, i).text() for i in range(self.ui.dataDisplay_tw.columnCount())]

    @staticmethod
    def get_model_name(model: BaseModel):
        return model._meta.table_name
    
    def refresh_data(self):
        data = select_all(self.curModel)
        self.tmanager.fill_table(data=data)

    @property
    def curTable(self):
        return self.tables[self.ui.currentTable_cb.currentIndex()]
    
    @property
    def curModel(self):
        return get_model[self.curTable]

    def get_table_columns(self, table: str):
        verbose_columns = get_verbose_columns(table)
        self.columns_types = {v_col: col_type for v_col, col_type in zip(verbose_columns, self.curModel._meta.fields.values())}
        return verbose_columns

    @Slot()
    def show_current_table(self):
        self.record_id = None
        columns = self.get_table_columns(self.curTable)
        data = select_all(self.curModel)
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
                inp.setDisplayFormat(u"yyyy-MM-dd")
                self.ui.inputs_hbl.addWidget(inp)
            elif isinstance(col_type, BooleanField):
                inp = QComboBox()
                inp.setObjectName("is_male")
                inp.addItems(["М", "Ж"])
                self.ui.inputs_hbl.addWidget(inp)
            elif isinstance(col_type, ForeignKeyField):
                inp = QComboBox()
                inp.setObjectName(col_name)
                first_col_dict = {data[1]: data[0] for data in select_all(get_model[col_type.backref])}
                self.foreign_keys_ids[col_name] = first_col_dict
                inp.addItems(first_col_dict.keys())
                self.ui.inputs_hbl.addWidget(inp)

    @Slot()
    def goto_menu(self):
        self.hide()
        self.data_manage_signals.goto_menu.emit()
    
    @Slot(User)
    def user_enters(self, user: User):
        self.user = user
        self.show()

    @staticmethod
    def clear_layout(layout: QHBoxLayout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()
