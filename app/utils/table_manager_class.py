from PySide6.QtWidgets import QTableWidget, QTableWidgetItem


class TableManager:

    def __init__(self, table: QTableWidget):
        self.table = table


    def fill_table(self, data, columns: list):
        self.table.setHorizontalHeaderLabels(columns)