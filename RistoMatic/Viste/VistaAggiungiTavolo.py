import datetime
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, \
    QCalendarWidget, QComboBox

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Tavolo import Tavolo


class VistaAggiungiTavolo(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiTavolo, self).__init__()
        self.callback = callback
        self.vLayout = QVBoxLayout()
        self.qlines = {}
        self.addInfoText("numeroPosti", "Numero posti massimi")
        self.addInfoText("riferimentoTavolo", "Numero tavolo")

        self.box = QCheckBox("Generare automaticamente il numero del tavolo? (il numero specificato sopra verrà ignorato)", self)

#        self.box.stateChanged.connect(self.clickBox)

        self.vLayout.addWidget(self.box)

        okButton = QPushButton("OK")
        tavolo = okButton.clicked.connect(self.aggiungiTavolo)
        self.qlines["okButton"] = okButton
        self.vLayout.addWidget(okButton)
        self.setLayout(self.vLayout)


    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)

    def aggiungiTavolo(self):
        print('aggiungiTavolo')
        numeroPosti = self.qlines["numeroPosti"].text()

        numero = self.qlines["riferimentoTavolo"].text()


        print(numero)
        check = self.box.checkState()
        if check != 2:  # se c'è la spunta il numero del tavolo viene generato automaticamente
            print('1')
            numero = int(numero)
            print(numero)
            numeroEsistente = False

            for tavolo in StatoSala.Tavoli:
                if tavolo.riferimentoTavolo == numero:
                    numeroEsistente = True
                    message = QMessageBox()
                    message.setIcon(QMessageBox.Critical)
                    message.setText('ERRORE!')
                    message.setInformativeText("Il numero scelto appartiene già ad un altro tavolo, cambia il numero scelto")
                    message.exec_()
                    return
            if numeroEsistente == False:
                tavolo = Tavolo(int(numeroPosti), numero)
        elif check == 2:
            print('2')
            tavolo = Tavolo(numeroPosti)

        self.close()


