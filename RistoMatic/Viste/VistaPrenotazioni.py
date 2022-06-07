from PySide6 import QtWidgets
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QPushButton, QSizePolicy, QHBoxLayout, QListView
from PySide6.QtWidgets import QVBoxLayout

from RistoMatic.Viste.ClasseTestLudovico import ClasseTestLudovico
from RistoMatic.Viste.VistaAggiungiPrenotazione import VistaAggiungiPrenotazione
from RistoMatic.Viste.VistaPrenotazione import VistaPrenotazione



class VistaPrenotazioni(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lista = ClasseTestLudovico()


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
        testButton.clicked.connect(self.lista.stampaLista)
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

        for prenotazione in self.lista.PRENOTAZIONI:  # per ogni prenotazione crea una riga
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
        prenotazione = self.lista.ricercaNomeRecapitoTavolo(nomeCliente, recapitoTelefonico, riferimentoTavolo)
        #prenotazione =
        self.vistaPrenotazione = VistaPrenotazione(prenotazione, eliminaCallback=self.aggiornaUi())
        self.vistaPrenotazione.show()


    def eliminaPrenotazione(self):
        print("eliminaPrenotazione")
        selected = self.listView.selectedIndexes()[0].data()
        nomeCliente = selected.split(', ')[0].strip()
        riferimentoTavolo = selected.split(', ')[3].strip().split()[1]
        dataPrenotazione = selected.split(', ')[1].strip()
        index = self.lista.ricercaNomeDataTavolo(nomeCliente, dataPrenotazione, riferimentoTavolo)
        del self.lista.PRENOTAZIONI[index]
        self.aggiornaUi()




    def aggiungiPrenotazione(self):
        print("aggiungiPrenotazione")
        self.inserisciPrenotazione = VistaAggiungiPrenotazione(callback=self.aggiornaUi)
        self.inserisciPrenotazione.show()



