from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QListView
from PySide6.examples.widgets.layouts.flowlayout.flowlayout import FlowLayout

from RistoMatic.Viste.ClasseTestLudovico import ClasseTestLudovico


class VistaAsporto(QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout = QGridLayout(self)
        self.lista = ClasseTestLudovico()
        self.addButton = QPushButton('Aggiungi ordine')
        self.delButton = QPushButton('Rimuovi ordine')

        self.addButton.clicked.connect(self.aggiungiOrdine)
        self.delButton.clicked.connect(self.rimuoviOrdine)

        self.bottomBox = QHBoxLayout()
        self.bottomBox.addWidget(self.addButton)
        self.bottomBox.addWidget(self.delButton)
#        bottomBox.addWidget(button3)


        self.gridLayout.addLayout(self.bottomBox, 10, 10)
#        self.gridLayout.addWidget(self.delButton)
        self.loadOrdini()
    def aggiungiOrdine(self):

        pass
    def rimuoviOrdine(self):
        pass

    def loadOrdini(self):
        #self.vlayout = QVBoxLayout()
        column = 1
        row = 1
        for ordine in self.lista.ASPORTO:
            self.vLayout = QVBoxLayout(self)
            self.setGeometry(100, 100, 100, 100)
            self.nome = QLabel("Nome: " + str(ordine.cliente.getNomeCliente()))
            self.recapito = QLabel('Telefono: ' + str(ordine.cliente.getRecapitoTelefonico()))
            self.oraConsegna = QLabel('Ora consegna: ' + str(ordine.getOraConsegna()))
            self.oraOrdine = QLabel('Ora ordine: ' + str(ordine.getoraOrdine()))
            self.vLayout.addWidget(self.nome)
            self.vLayout.addWidget(self.recapito)
            self.vLayout.addWidget(self.oraConsegna)
            self.vLayout.addWidget(self.oraOrdine)
            self.gridLayout.addLayout(self.vLayout, row, column, row, column)
            column += 1
            if column == 11:
                column = 1
                row += 1
            self.listaElementi = QListView()
            for ordine in self.lista.ASPORTO:
                item = QStandardItem()
                for elemento in ordine.comanda.elementiComanda:
                    titolo = f"{elemento.ElementoMenu.getNomeElemento(), elemento.getQuantita}"
                    item.setText(titolo)
                    item.setEditable(False)
                    font = item.font()
                    font.setPointSize(12)
                    item.setFont(font)
                    self.listaElementi.appendRow(item)


