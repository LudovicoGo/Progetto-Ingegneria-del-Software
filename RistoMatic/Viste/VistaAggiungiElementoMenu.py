from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton


class VistaAggiungiElementoMenu(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.vLayout =QVBoxLayout()
        self.qlines = {}

        self.addInfoText("nomeElemento", "Nome pietanza/bevanda")
        self.addInfoText("areaPreparazione", "Area di preparazione")
        self.addInfoText("prezzoElemento", "Prezzo pietanza/bevanda")

        self.salvaElemento = QPushButton('Aggiungi Elemento al Menù')
        self.salvaElemento.clicked.connect(self.saveElemento)
        self.vLayout.addWidget(self.salvaElemento)



    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)

    def saveElemento(self):
        pass
