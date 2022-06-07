from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione
from RistoMatic.Viste.ClasseTestLudovico import ClasseTestLudovico


class VistaAggiungiPrenotazione(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiPrenotazione, self).__init__()
        #self.lista = ClasseTestLudovico()

        self.callback = callback
        self.vLayout = QVBoxLayout()
        self.qlines = {}
        self.addInfoText("nome", "Nome")
        self.addInfoText("dataPrenotazione", "Data")
        self.addInfoText("numeroPersone", "Numero Persone")
        self.addInfoText("riferimentoTavolo", "Riferimento Tavolo")
        self.addInfoText("recapitoTelefonico", "Recapito Telefonico")

        okButton = QPushButton("OK")
        okButton.clicked.connect(self.aggiungiPrenotazione)
        self.qlines["okButton"] = okButton
        self.vLayout.addWidget(okButton)
        self.setLayout(self.vLayout)


    def addInfoText(self,nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)


    def aggiungiPrenotazione(self):
        try:
            riferimentoTavolo = int(self.qlines["riferimentoTavolo"].text())

        except:
            QMessageBox.critical(self, 'ERRORE! il numero del tavolo non è valido', QMessageBox.Ok, QMessageBox.Ok)
            return

        for value in self.qlines.values():
            if isinstance(value, QLineEdit):
                if value.text() == "":
                    QMessageBox.critical(self, 'ERRORE! informazioni mancanti', QMessageBox.Ok, QMessageBox.Ok)
                    return

        cliente = Cliente("", "")
        prenotazione = Prenotazione('', -1, '', cliente, -1)

        try:
            nome = self.qlines["nome"].text()
            recapitoTelefonico = self.qlines["recapitoTelefonico"].text()
            dataPrenotazione = self.qlines["dataPrenotazione"].text()
            numeroPersone = int(self.qlines["numeroPersone"].text())

            prenotazione.setDataPrenotazione(dataPrenotazione)
            prenotazione.setRiferimentoTavolo(riferimentoTavolo)
            prenotazione.setNumeroPersone(numeroPersone)
            prenotazione.cliente.setNomeCliente(nome)
            prenotazione.cliente.setRecapitoTelefonico(recapitoTelefonico)




        except:
            QMessageBox.critical(self, 'ERRORE! Controllare i dati inseriti', QMessageBox.Ok, QMessageBox.Ok)
            return

        self.callback()
        self.close()
        return prenotazione
