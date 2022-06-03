from PySide6 import QtWidgets
from random import *
from PySide6.QtCore import Signal,Slot
from RistoMatic.Viste.Blocks.BlockDettaglioTavolo import VistaTavolo
from RistoMatic.Viste.Blocks._BlockElementiComanda import BlockListaElementiComanda
from RistoMatic.GestioneAttivita.Enum import StatoTavolo

class BlockTavolo(QtWidgets.QPushButton):

    update_ui=Signal()
    def __init__(self,num,stat):
        super().__init__()

        self.num = num
        self.detail=VistaTavolo()

        self.setText(f"Tavolo {num} \n Coperti: {randint(0,10)} \n Status: {stat}")

        if (stat == StatoTavolo.UTILIZZABILE):
            self.setStyleSheet('QPushButton {background-color: green; font-size: 16px; height: 90; width:150;}')
        elif (stat == StatoTavolo.PRENOTATO):
            self.setStyleSheet('QPushButton {background-color: orange; font-size: 16px; height: 90; width:150;}')
            self.setText(self.text() + "\n Nome Cognome \n 3332323232")
        elif(stat == StatoTavolo.OCCUPATO):
            self.setStyleSheet('QPushButton {background-color: red; font-size: 16px; height: 90; width:150;}')

        self.clicked.connect(self.show_detail)

    def show_detail(self):
        self.detail.crea(BlockListaElementiComanda())
        self.detail.show()
        self.update_ui.emit()


