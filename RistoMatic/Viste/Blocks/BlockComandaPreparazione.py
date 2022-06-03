from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Slot,Signal
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.Viste.Blocks.BlockElementoComanda import BlockElementoComanda

class BlockComandaPreparazione(QtWidgets.QGroupBox):

    def __init__(self, comanda: Comanda):
        super().__init__(f"Comanda {comanda.numeroComanda} - Tavolo {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)

        for elem in comanda.elementiComanda:
            btn = BlockElementoComanda(elem, comanda)
            self.vbox.addWidget(btn)

        self.setLayout(self.vbox)

