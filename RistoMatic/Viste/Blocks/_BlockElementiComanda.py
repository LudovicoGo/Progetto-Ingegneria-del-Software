from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem
from random import *

class BlockListaElementiComanda(QtWidgets.QTableWidget):

    def __init__(self):
        super().__init__()
        # Column count
        self.setColumnCount(4)
        self.setRowCount(10)

        for i in range(0,10):
            self.setItem(i,0,QTableWidgetItem("cibo"))
            self.setItem(i, 1, QTableWidgetItem(""))
            self.setItem(i, 2, QTableWidgetItem(str(randint(1,10))))
            self.setItem(i, 3, QTableWidgetItem(str(randint(1,10))))

