from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Slot,Signal
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.Viste.Blocks.BlockElementoComanda import BlockElementoComanda
from RistoMatic.GestioneAttivita.Tavolo import Tavolo

class BlockComandaPreparazione(QtWidgets.QGroupBox):

    def __init__(self, comanda: Comanda):
        if(isinstance(comanda.rif,Tavolo)):
            super().__init__(f"Comanda {comanda.numeroComanda} - Tavolo {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
        else:
            super().__init__(f"Comanda {comanda.numeroComanda} - Asporto {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
            self.setStyleSheet("QGroupBox {background-color: blue;}")
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)

        for elem in comanda.elementiComanda:
            if not elem.getIsPronta():
                btn = BlockElementoComanda(elem, comanda)
                self.vbox.addWidget(btn)

        self.setLayout(self.vbox)

