from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QAbstractItemView, QGridLayout, QPushButton, QSizePolicy, QHBoxLayout, QListView
from PySide6.QtWidgets import QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem

from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione


class VistaPrenotazioni(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.cliente = Cliente('Albertino', '3333333333')
        self.cliente2 = Cliente('Michelino', '3333333333')
        self.cliente3 = Cliente('Faustino', '3333333333')

        self.PRENOTAZIONI = [Prenotazione('Oggi', 5, 'Confermata', self.cliente, 4),
                             Prenotazione('Oggi', 1, 'Da Confermare', self.cliente3, 10),
                             Prenotazione('Oggi', 3, 'Da Confermare', self.cliente2, 6),
                             Prenotazione('Oggi', 17, 'Confermata', self.cliente, 2),
                             Prenotazione('Oggi', 14, 'Confermata', self.cliente3, 44),
                             Prenotazione('Oggi', 6, 'Confermata', self.cliente2, 47),
                             Prenotazione('Oggi', 8, 'Confermata', self.cliente2, 47),
                             Prenotazione(dataPrenotazione='Oggi', numeroPersone=21, statoPrenotazione='Confermata', cliente=self.cliente2, riferimentoTavolo=7)]

        self.PRENOTAZIONI.sort(key=lambda x: x.cliente.getNomeCliente())       #mette in ordine alfabetico le prenotazioni riferendosi al nome dei clienti che le hanno effettuate

        hLayout = QHBoxLayout()
        self.listView = QListView()
        self.aggiornaUi()
        hLayout.addWidget(self.listView)

        buttonsLayout = QVBoxLayout()
        modifyButton = QPushButton("Modifica Prenotazione")
        modifyButton.clicked.connect(self.modificaPrenotazione)

        newButton = QPushButton("Aggiungi Prenotazione")
        newButton.clicked.connect(self.aggiungiPrenotazione)

        delButton = QPushButton("Elimina Prenotazione")
        delButton.clicked.connect(self.eliminaPrenotazione)

        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(modifyButton)
        buttonsLayout.addWidget(delButton)

        buttonsLayout.addStretch()
        hLayout.addLayout(buttonsLayout)



        self.setLayout(hLayout)
        self.resize(600, 300)
        self.setWindowTitle("Prenotazioni")



    def aggiornaUi(self):
       # self.pren = []
       # self.loadPrenotazioni()
        listViewModel = QStandardItemModel(self.listView)

        for prenotazione in self.PRENOTAZIONI: #per ogni prenotazione crea una riga
            item = QStandardItem()
            titolo = f"{prenotazione.cliente.getNomeCliente()},  {prenotazione.getDataPrenotazione()},  Coperti: {prenotazione.getNumeroPersone()},  Tavolo: {prenotazione.getRiferimentoTavolo()}"
            item.setText(titolo)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(20)
            item.setFont(font)
            listViewModel.appendRow(item)

        self.listView.setModel(listViewModel)








    def getGenericButton(self, titolo, onClick):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(onClick)
        return


    def modificaPrenotazione(self):
        print("modificaPrenotazione")

    def aggiungiPrenotazione(self):
        print("aggiungiPrenotazione")

    def eliminaPrenotazione(self):
        print("eliminaPrenotazione")


