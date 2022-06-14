from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, \
    QCalendarWidget, QComboBox

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione

class VistaAggiungiPrenotazione(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiPrenotazione, self).__init__()

        self.callback = callback
        self.vLayout = QVBoxLayout()
        self.qlines = {}
        self.addInfoText("nome", "Nome")
        #self.addInfoText("dataPrenotazione", "Data")
        self.addInfoText("numeroPersone", "Numero Persone")
        self.addInfoText("riferimentoTavolo", "Riferimento Tavolo")
        self.addInfoText("recapitoTelefonico", "Recapito Telefonico")

        self.data = QCalendarWidget()
        self.data.clicked.connect(self.selezionaData)
        self.dataSelezionata = None

        self.menuOra = QComboBox()
        orari = ['11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30']
        self.menuOra.addItems(orari)
   #    self.menuOra.clicked.connect(self)

        self.dataString = QLabel("Giorno prenotazione:")
        self.oraString = QLabel("Orario prenotazione:")
        self.box = QCheckBox("Prenotazione da confermare?", self)
        self.box.stateChanged.connect(self.clickBox)
        self.vLayout.addWidget(self.dataString)
        self.vLayout.addWidget(self.data)
        self.vLayout.addWidget(self.oraString)
        self.vLayout.addWidget(self.menuOra)

        self.vLayout.addWidget(self.box)



        self.statoPrenotazione = "Confermata"

        okButton = QPushButton("OK")
        prenotazione = okButton.clicked.connect(self.aggiungiPrenotazione)
        self.qlines["okButton"] = okButton
        self.vLayout.addWidget(okButton)
        self.setLayout(self.vLayout)

    def selezionaData(self):
        self.dataSelezionata = self.data.selectedDate()

    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)


    def aggiungiPrenotazione(self):

        riferimentoTavolo = int(self.qlines["riferimentoTavolo"].text())


        cliente = Cliente("", "")
        prenotazione = Prenotazione('', -1, '', cliente, -1)


        nome = self.qlines["nome"].text()
        recapitoTelefonico = self.qlines["recapitoTelefonico"].text()

        dataPrenotazione = self.dataSelezionata

        #dataPrenotazione = self.qlines["dataPrenotazione"].text()
        numeroPersone = int(self.qlines["numeroPersone"].text())
        statoPrenotazione = self.statoPrenotazione



        prenotazione.setDataPrenotazione(dataPrenotazione)
        prenotazione.setRiferimentoTavolo(riferimentoTavolo)
        prenotazione.setNumeroPersone(numeroPersone)
        prenotazione.setStatoPrenotazione(statoPrenotazione)
        prenotazione.cliente.setNomeCliente(nome)
        prenotazione.cliente.setRecapitoTelefonico(recapitoTelefonico)

        StatoSala.Prenotazioni.append(prenotazione)
        self.close()

    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Da confermare')
            self.statoPrenotazione = "Non Confermata"

        else:
            print('Da confermare')
            self.statoPrenotazione = "Confermata"
