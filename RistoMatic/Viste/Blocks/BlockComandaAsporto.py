from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QListView
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.Viste.Blocks.BlockElementoComandaSala import BlockElementoComandaSala
from RistoMatic.Viste.VistaAggiungiElemento import VistaAggiungiElemento

from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.Viste.Blocks.BlockElementoComandaAsporto import BlockElementoComandaAsporto
from RistoMatic.Viste.VistaAggiungiElemento import VistaAggiungiElemento
from RistoMatic.Viste.VistaAggiungiElementoAsporto import VistaAggiungiElementoAsporto


class BlockComandaAsporto(QtWidgets.QGroupBox):

    def __init__(self, ordine : OrdineAsporto):
        super().__init__()
        self.ordine = ordine
        self.setTitle("Ordine Asporto: "+ ordine.cliente.nomeCliente + "   Ora Consegna " + ordine.oraConsegna)
       # if (isinstance(comanda.rif, Tavolo)):
       #     self.setTitle(
       #         f"Comanda {comanda.numeroComanda} - Tavolo {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
       # else:
             #self.setTitlef("Comanda {ordine.numeroOrdine} - Asporto  - {ordine.oraConsegna}")
             #self.setStyleSheet("QGroupBox {background-color: blue;}")

        self.setMinimumWidth(300)
        self.setMinimumHeight(300)
        self.vbox = QVBoxLayout()

        self.addButton = QPushButton("Aggiungi elemento")
        self.addButton.clicked.connect(self.aggiungiElemento)
        self.vbox.addWidget(self.addButton)

        #self.vbox.addStretch(1)
        self.list = QVBoxLayout()
        self.listview = QListView()
        self.lista = QStandardItemModel(self.listview)
        for ordinato in ordine.comanda.elementiComanda:
            item = QStandardItem()
            title = f"{ordinato.elemento.nomeElemento}, Q.tà: {ordinato.quantita}, Prezzo: {ordinato.elemento.prezzoElemento}x{ordinato.quantita}"
            item.setText(title)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.lista.appendRow(item)


        self.listview.setModel(self.lista)

        self.vbox.addWidget(self.listview)

        self.totline = QHBoxLayout()



        self.tot = QLabel("Totale: "+ str(self.ordine.comanda.getTotale()) +" €")
        self.tot.setStyleSheet("QLabel {font-size:16px; font-weight: bold}")
        self.totline.addWidget(self.tot)
        self.totline.setAlignment(Qt.AlignRight)
        self.vbox.addLayout(self.totline)

        self.delButton = QPushButton("Rimuovi elemento")
        self.delButton.clicked.connect(self.rimuoviElemento)
        self.vbox.addWidget(self.delButton)

        self.stampa = QPushButton("Stampa Conto")
        self.stampa.clicked.connect(self.stampaConto)
        self.vbox.addWidget(self.stampa)
        self.setLayout(self.vbox)

        self.waggiungi=None

    def aggiornaTotale(self):
        self.tot.setText("Totale: "+ str(self.ordine.comanda.getTotale()) +" €")
        pass

    def aggiungiElemento(self):
        self.waggiungi=VistaAggiungiElementoAsporto(self.ordine)
        self.waggiungi.update_ui.connect(self.aggiungiBlock)
        self.waggiungi.show()

    def aggiungiBlock(self):
        block = BlockElementoComandaAsporto(self.ordine.comanda.elementiComanda[-1])
        block.aggiornaComanda.connect(self.aggiornaTotale)
        block.eliminaElemento.connect(self.eliminaElemento)
        self.list.addLayout(block)
        self.aggiornaTotale()

    def rimuoviElemento(self,elemento):
        self.ordine.comanda.rimuoviElementoComanda(elemento)

    def stampaConto(self):
        print('Stampa conto')
