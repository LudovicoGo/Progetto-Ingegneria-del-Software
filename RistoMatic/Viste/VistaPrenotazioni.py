from PySide6 import QtWidgets
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



        lenght = len(self.PRENOTAZIONI)
        self.table = QTableWidget(lenght, 6)
        self.table.setObjectName('table')
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        i = 0
        for prenotazione in self.PRENOTAZIONI:
            self.table.setItem(i, 0, QTableWidgetItem(prenotazione.cliente.getNomeCliente()))
            self.table.setItem(i, 1, QTableWidgetItem(prenotazione.getDataPrenotazione()))
            self.table.setItem(i, 2, QTableWidgetItem(str(prenotazione.getNumeroPersone())))
            self.table.setItem(i, 3, QTableWidgetItem(str(prenotazione.getRiferimentoTavolo())))
            self.table.setItem(i, 4, QTableWidgetItem(prenotazione.cliente.getRecapitoTelefonico()))
            self.table.setItem(i, 5, QTableWidgetItem(prenotazione.getStatoPrenotazione()))
            i += 1
            self.table.insertRow(self.table.rowCount())
            if i == (len(self.PRENOTAZIONI)):
                i = 0
                break





        self.row = QGridLayout()
        self.title = QLabel(f"Prenotazioni odierne")
        self.title.setStyleSheet("QLabel {font-size: 20px;}")
        self.row.addWidget(self.title, 0, 0)
        self.row.addWidget(self.table, 1, 0)
        #self.row.addWidget(self.getGenericButton('Elimina Prenotazione', self.EliminaPrenotazione()), 2, 0, 1,2)

        self.setLayout(self.row)





    def getGenericButton(self, titolo, onClick):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(onClick)
        return

    def AggiungiPrenotazione(self):
        pass


    def EliminaPrenotazione(self):
        pass


