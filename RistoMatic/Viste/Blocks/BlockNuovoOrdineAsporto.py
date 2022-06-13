from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QPushButton

from RistoMatic.GestioneAttivita import OrdineAsporto


class BlockNuovoOrdineAsporto(QtWidgets.QGroupBox):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(300, 227)
        self.vbox = QVBoxLayout()

        self.addbtn = QPushButton("Aggiungi Nuovo Ordine ")
        self.addbtn.clicked.connect(self.aggiungiNuovoOrdine)
        self.vbox.addWidget(self.addbtn)
        self.setLayout(self.vbox)

    def aggiungiNuovoOrdine(self):
        pass
