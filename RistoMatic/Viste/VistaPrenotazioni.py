from collections import defaultdict

from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QPushButton, QSizePolicy, QHBoxLayout, QListView
from PySide6.QtWidgets import QVBoxLayout

from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione
from RistoMatic.Viste.VistaAggiungiPrenotazione import VistaAggiungiPrenotazione
from RistoMatic.Viste.VistaPrenotazione import VistaPrenotazione


class VistaPrenotazioni(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.cliente = Cliente('Albertino', '987654321')
        self.cliente2 = Cliente('Michelino', '123456789')
        self.cliente3 = Cliente('Faustino', '123789456')

        self.PRENOTAZIONI = [Prenotazione('dd/mm/yyyy', 5, 'Confermata', self.cliente, 4),
                             Prenotazione('dd/mm/yyyy', 1, 'Da Confermare', self.cliente3, 10),
                             Prenotazione('dd/mm/yyyy', 3, 'Da Confermare', self.cliente2, 6),
                             Prenotazione('dd/mm/yyyy', 17, 'Confermata', self.cliente, 2),
                             Prenotazione('dd/mm/yyyy', 14, 'Confermata', self.cliente3, 44),
                             Prenotazione('dd/mm/yyyy', 6, 'Confermata', self.cliente2, 47),
                             Prenotazione('dd/mm/yyyy', 8, 'Confermata', self.cliente2, 887),
                             Prenotazione(dataPrenotazione='Oggi', numeroPersone=21, statoPrenotazione='Confermata',
                                          cliente=self.cliente2, riferimentoTavolo=7)]

        #self.PRENOTAZIONI.sort(key=lambda x: x.cliente.getNomeCliente())  # mette in ordine alfabetico le prenotazioni riferendosi al nome dei clienti che le hanno effettuate

        hLayout = QHBoxLayout()
        self.listView = QListView()
        self.aggiornaUi()
        hLayout.addWidget(self.listView)

        buttonsLayout = QVBoxLayout()
        infoButton = QPushButton("Visualizza altro")
        infoButton.clicked.connect(self.visualizzaAltro)

        newButton = QPushButton("Aggiungi Prenotazione")
        newButton.clicked.connect(self.aggiungiPrenotazione)

        delButton = QPushButton("Elimina Prenotazione")
        delButton.clicked.connect(self.eliminaPrenotazione)

        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(infoButton)
        buttonsLayout.addWidget(delButton)


        ##############################################
        testButton = QPushButton("TEST (stampa lista)")
        delButton.clicked.connect(self.stampaLista)
        buttonsLayout.addWidget(testButton)
        ##############################################

        buttonsLayout.addStretch()
        hLayout.addLayout(buttonsLayout)

        self.setLayout(hLayout)
        self.resize(600, 300)
        self.setWindowTitle("Prenotazioni")

    def loadPrenotazioni(self):
        pass

    def aggiornaUi(self):
        listViewModel = QStandardItemModel(self.listView)

        for prenotazione in self.PRENOTAZIONI:  # per ogni prenotazione crea una riga
            item = QStandardItem()
            titolo = f"{prenotazione.cliente.getNomeCliente()},  {prenotazione.getDataPrenotazione()},  Coperti: {prenotazione.getNumeroPersone()}, Tavolo: {prenotazione.getRiferimentoTavolo()}, Numero telefono: {prenotazione.cliente.getRecapitoTelefonico()}"
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

    def visualizzaAltro(self):

        selected = self.listView.selectedIndexes()[0].data()

        nomeCliente = selected.split(', ')[0].strip()
        riferimentoTavolo = selected.split(', ')[3].strip().split()[1]
        recapitoTelefonico = selected.split(', ')[4].strip().split()[2]

        print(nomeCliente)
        print(recapitoTelefonico)

        prenotazione = self.ricercaNomeRecapitoTavolo(nomeCliente, recapitoTelefonico, riferimentoTavolo)

        self.vistaPrenotazione = VistaPrenotazione(prenotazione, eliminaCallback=self.aggiornaUi())
        self.vistaPrenotazione.show()

    def eliminaPrenotazione(self):
        print("eliminaPrenotazione")
        selected = self.listView.selectedIndexes()[0].data()

        nomeCliente = selected.split(', ')[0].strip()
        riferimentoTavolo = selected.split(', ')[3].strip().split()[1]
        dataPrenotazione = selected.split(', ')[1].strip()

        index = self.ricercaNomeDataTavolo(nomeCliente, dataPrenotazione, riferimentoTavolo)
        del self.PRENOTAZIONI[index]
        self.aggiornaUi()




    def aggiungiPrenotazione(self):
        print("aggiungiPrenotazione")
        self.inserisciPrenotazione = VistaAggiungiPrenotazione(callback=self.aggiornaUi)
        self.inserisciPrenotazione.show()





    def ricercaNomeDataTavolo(self, nomeCliente, dataPrenotazione, riferimentoTavolo):
        for i in range(0, len(self.PRENOTAZIONI)):
            if self.PRENOTAZIONI[i].cliente.nomeCliente == nomeCliente and self.PRENOTAZIONI[i].dataPrenotazione == dataPrenotazione and self.PRENOTAZIONI[i].riferimentoTavolo == riferimentoTavolo:
                return i
            i = i+1
        return -1


    def ricercaNomeRecapitoTavolo(self, nomeCliente, recapitoTelefonico, riferimentoTavolo):
       for i in self.PRENOTAZIONI:
            if i.cliente.nomeCliente == nomeCliente and i.riferimentoTavolo == int(riferimentoTavolo):
                prenotazione = i
       return prenotazione


    #classe per test
    def stampaLista(self):
        for i in self.PRENOTAZIONI:
            print(i.getInfoPrenotazione())
