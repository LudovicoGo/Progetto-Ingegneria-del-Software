from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione

class VistaAggiungiPrenotazione(QWidget):

    def __init__(self, callback, lista):
        super(VistaAggiungiPrenotazione, self).__init__()

        self.callback = callback
        self.lista = lista
        self.vLayout = QVBoxLayout()
        self.qlines = {}
        self.addInfoText("nome", "Nome")
        self.addInfoText("dataPrenotazione", "Data")
        self.addInfoText("numeroPersone", "Numero Persone")
        self.addInfoText("riferimentoTavolo", "Riferimento Tavolo")
        self.addInfoText("recapitoTelefonico", "Recapito Telefonico")

        okButton = QPushButton("OK")
        prenotazione = okButton.clicked.connect(self.aggiungiPrenotazione)
        self.qlines["okButton"] = okButton
        self.vLayout.addWidget(okButton)
        self.setLayout(self.vLayout)

    def addInfoText(self,nome, label):
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
        dataPrenotazione = self.qlines["dataPrenotazione"].text()
        numeroPersone = int(self.qlines["numeroPersone"].text())
        prenotazione.setDataPrenotazione(dataPrenotazione)
        prenotazione.setRiferimentoTavolo(riferimentoTavolo)
        prenotazione.setNumeroPersone(numeroPersone)
        prenotazione.cliente.setNomeCliente(nome)
        prenotazione.cliente.setRecapitoTelefonico(recapitoTelefonico)

        self.lista.append(prenotazione)
        self.close()
