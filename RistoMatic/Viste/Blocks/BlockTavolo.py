from PySide6 import QtWidgets
from random import *
from PySide6.QtCore import Signal, Slot, QTimer
from RistoMatic.Viste.Blocks.BlockDettaglioTavolo import VistaTavolo
from RistoMatic.Viste.Blocks._BlockElementiComanda import BlockListaElementiComanda
from RistoMatic.GestioneAttivita.Enum import StatoTavolo

class BlockTavolo(QtWidgets.QPushButton):

    #update_ui=Signal()

    def __init__(self,tavolo):
        super().__init__()

        self.tavolo = tavolo

        self.detail=VistaTavolo()
        self.timer = QTimer()
        self.timer.timeout.connect(self.aggiorna)
        self.timer.start(5000)

        self.status = tavolo.getStato()
        self.filldata()

        self.clicked.connect(self.show_detail)

    def show_detail(self):
        self.detail.crea(BlockListaElementiComanda())
        self.detail.show()
        #self.update_ui.emit()


    @Slot()
    def aggiorna(self):
        self.filldata()

    def filldata(self):
        self.status = self.tavolo.getStato()
        self.setText(
            f"Tavolo {str(self.tavolo.riferimentoTavolo)} \n Coperti: {str(self.tavolo.coperti)} \n Stato: {str(self.status.value)}")

        if (self.status == StatoTavolo.UTILIZZABILE):
            self.setStyleSheet('QPushButton {background-color: green; font-size: 16px; height: 90; width:150;}')
        elif (self.status == StatoTavolo.PRENOTATO):
            self.setStyleSheet('QPushButton {background-color: orange; font-size: 16px; height: 90; width:150;}')
            self.setText(self.text() + "\n Nome Cognome \n 3332323232")
        elif (self.status == StatoTavolo.OCCUPATO):
            self.setStyleSheet('QPushButton {background-color: red; font-size: 16px; height: 90; width:150;}')