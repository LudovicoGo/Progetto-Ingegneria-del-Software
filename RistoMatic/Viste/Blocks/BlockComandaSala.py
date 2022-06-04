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
        self.addbtn = QPushButton("Aggiungi elemento")
        self.addbtn.clicked.connect(self.aggiungi_elemento)
        self.vbox.addWidget(self.addbtn)
        #self.vbox.addStretch(1)

        for elemento in comanda.elementiComanda:
            block = BlockElementoComandaSala(elemento)
            block.aggiorna_comanda.connect(self.aggiorna_totale)
            block.elimina_elemento.connect(self.elimina_elemento)
            self.vbox.addLayout(block)

        self.totline = QHBoxLayout()
        self.tot = QLabel("Totale: "+ str(self.comanda.getTotale()) +" €")
        self.tot.setStyleSheet("QLabel {font-size:16px; font-weight: bold}")
        self.totline.addWidget(self.tot)
        self.totline.setAlignment(Qt.AlignRight)
        self.vbox.addLayout(self.totline)
        self.setLayout(self.vbox)

    def aggiorna_totale(self):
        self.tot.setText("Totale: "+ str(self.comanda.getTotale()) +" €")

    def aggiungi_elemento(self):
        pass

    def elimina_elemento(self,elemento,block):
        self.comanda.rimuoviElementoComanda(elemento)
