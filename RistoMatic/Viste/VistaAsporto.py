from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QPushButton, QLabel, QVBoxLayout

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
        column = 1
        row = 1
        for ordine in self.lista.ASPORTO:
            self.hLayout = QVBoxLayout(self)
            self.nome = QLabel("Nome: " + str(ordine.cliente.getNomeCliente()))
            self.recapito = QLabel('Telefono: ' + str(ordine.cliente.getRecapitoTelefonico()))
            self.oraConsegna = QLabel('Ora consegna: ' + str(ordine.getOraConsegna()))
            self.oraOrdine = QLabel('Ora ordine: ' + str(ordine.getoraOrdine()))
            self.hLayout.addWidget(self.nome)
            self.hLayout.addWidget(self.recapito)
            self.hLayout.addWidget(self.oraConsegna)
            self.hLayout.addWidget(self.oraOrdine)
            self.gridLayout.addLayout(self.hLayout, row, column, row, column)
            column += 1
            if column == 11:
                column = 1
                row += 1




