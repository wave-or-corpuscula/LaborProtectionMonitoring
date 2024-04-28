from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtWidgets import QHeaderView

class TableManager:

    def __init__(self, table: QTableWidget):
        self.table = table

    def fill_table(self, data: list[list], columns: list = None):
        if columns:
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.table.setColumnCount(len(columns))
            self.table.setHorizontalHeaderLabels(columns)
            self.table.setColumnHidden(0, 1)

        rows = len(data)
        self.table.setRowCount(rows)
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(col_data)))