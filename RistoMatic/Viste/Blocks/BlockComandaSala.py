from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout,QListWidget,QListWidgetItem, QHBoxLayout, QLabel,QLineEdit, QSizePolicy
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.Viste.Blocks.BlockElementoComandaSala import BlockElementoComandaSala
from RistoMatic.Viste.Blocks.LineSeparator import QHSeperationLine


class BlockComandaSala(QtWidgets.QGroupBox):

    def __init__(self, comanda: Comanda):
        super().__init__()
        self.comanda = comanda

        if (isinstance(comanda.rif, Tavolo)):
            self.setTitle(
                f"Comanda {comanda.numeroComanda} - Tavolo {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
        else:
            self.setTitle(
                f"Comanda {comanda.numeroComanda} - Asporto {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
            self.setStyleSheet("QGroupBox {background-color: blue;}")

        self.setMinimumWidth(300)

        self.vbox = QVBoxLayout()
        #self.vbox.addStretch(1)

        for elemento in comanda.elementiComanda:
            block = BlockElementoComandaSala(elemento)
            block.aggiorna_comanda.connect(self.aggiorna_totale)
            self.vbox.addLayout(block)

        self.totline = QHBoxLayout()
        self.tot = QLabel("Totale: "+ str(self.comanda.getTotale()) +" €")
        self.totline.addWidget(self.tot)
        self.totline.setAlignment(Qt.AlignRight)
        self.vbox.addLayout(self.totline)
        self.setLayout(self.vbox)

    def aggiorna_totale(self):
        self.tot.setText("Totale: "+ str(self.comanda.getTotale()) +" €")
