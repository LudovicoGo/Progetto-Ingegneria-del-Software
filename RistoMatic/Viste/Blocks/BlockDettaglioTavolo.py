from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel, QGridLayout

from RistoMatic.Viste.Blocks.BlockComandaSala import BlockComandaSala
from RistoMatic.GestioneAttivita.Comanda import Comanda


class BlockDettaglioTavolo(QtWidgets.QWidget):

    def __init__(self,tavolo):
        super().__init__()
        self.setWindowTitle(f"Tavolo {tavolo.riferimentoTavolo}")
        self.tavolo=tavolo
        self.add=QPushButton("aggiungi")
        self.remove = QPushButton("rimuovi")
        self.stampa = QPushButton("stampa preconto")

        self.comanda=Comanda.ricercaComanda(self.tavolo.riferimentoTavolo)

        self.wcomanda=None

        if (not self.comanda == None):
            self.wcomanda = BlockComandaSala(self.comanda)

        self.resize(540, 640)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.add,0,0,1,1)
        self.grid.addWidget(self.remove,0,1,1,1)
        self.grid.addWidget(self.wcomanda, 1, 0, 1, 2)
        self.grid.addWidget(self.stampa,2,0,1,1)


    def crea(self, comanda):
        pass

