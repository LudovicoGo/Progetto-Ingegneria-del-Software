from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel, QGridLayout


class VistaTavolo(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.title=QLabel("Tavolo 2")
        self.add=QPushButton("aggiungi")
        self.remove = QPushButton("rimuovi")
        self.stampa = QPushButton("stampa preconto")
        self.tot = QLabel("Totale: ")
        self.comanda = None

        self.resize(540, 640)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.title,0,0,1,2)
        self.grid.addWidget(self.add,1,0,1,1)
        self.grid.addWidget(self.remove,1,1,1,1)
        self.grid.addWidget(self.stampa,3,0,1,1)
        self.grid.addWidget(self.tot, 3, 1, 1, 1)

    def crea(self, comanda):
        self.comanda = comanda
        self.grid.addWidget(self.comanda,2,0,1,2)
