from PySide6 import QtWidgets
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem


class VistaPrenotazioni(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.table = QTableWidget(1,5)
        self.table.setObjectName('table')
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)


        self.table.setItem(0,0,QTableWidgetItem("asd"))
        self.table.setItem(0, 1, QTableWidgetItem("asd"))
        self.table.setItem(0, 2, QTableWidgetItem("333333"))
        self.table.setItem(0, 3, QTableWidgetItem("20:30 domenica 23 maggio 2022"))
        self.table.setItem(0, 4, QTableWidgetItem("7"))
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem("asd"))
        self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem("asd"))
        self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem("333333"))
        self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem("20:30 domenica 23 maggio 2022"))
        self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem("7"))
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem("asd"))
        self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem("asd"))
        self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem("333333"))
        self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem("20:30 domenica 23 maggio 2022"))
        self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem("7"))



        self.row = QVBoxLayout()
        self.title = QLabel(f"Prenotazioni odierne")
        self.title.setStyleSheet("QLabel {font-size: 16px;}")
        self.row.addWidget(self.title)
        self.row.addWidget(self.table)

        self.setLayout(self.row)
