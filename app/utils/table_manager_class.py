from PySide6.QtCore import QDate
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView


class TableManager:

    def __init__(self, table: QTableWidget, hidden_cols: list = None):
        self.table = table
        self.hidden_cols = hidden_cols

    def fill_with_filter(self, data: list[list], filter: str = None):
        if filter:
            self.table.setRowCount(0)
            filter = filter.lower()  # Приведение фильтра к нижнему регистру для корректного сравнения
            for row_data in data:
                table_row = []
                insert_row = False
                for col_data in row_data:
                    item = QTableWidgetItem(str(col_data))
                    table_row.append(item)
                    if filter in str(col_data).lower():
                        insert_row = True
                if insert_row:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    for col, item in enumerate(table_row):
                        self.table.setItem(row_position, col, item)
        else:
            self.fill_table(data)
    
    def fill_with_date_filter(self, data: list[list], start_date: QDate, end_date: QDate, date_column_index: int):
        self.table.setRowCount(0)
        for row_data in data:
            date_str = row_data[date_column_index]
            date = QDate.fromString(date_str, "yyyy-MM-dd")
            
            if start_date <= date <= end_date:
                table_row = [QTableWidgetItem(str(col_data)) for col_data in row_data]
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                for col, item in enumerate(table_row):
                    self.table.setItem(row_position, col, item)

    def fill_table(self, data: list[list], columns: list = None):
        if columns:
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.table.setColumnCount(len(columns))
            self.table.setHorizontalHeaderLabels(columns)
            if self.hidden_cols:
                for col in self.hidden_cols:
                    self.table.setColumnHidden(col, 1)

        rows = len(data)
        self.table.setRowCount(rows)
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(col_data)))
