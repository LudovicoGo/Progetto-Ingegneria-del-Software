from RistoMatic.Viste.FlowLayout import FlowLayout
from random import *
from RistoMatic.Viste.Blocks.BlockTavolo import BlockTavolo
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from PySide6 import QtWidgets
from PySide6.QtCore import Signal,Slot, QTimer

class VistaTavoli(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.layout = FlowLayout(self)
        self.contatore = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.aggiornaUi)
        self.timer.start(5000)


    def aggiornaUi(self):
        StatoSala.Tavoli.sort(key=lambda x: x.getRiferimentoTavolo())
        lenght = len(StatoSala.Tavoli)

        if self.contatore < lenght:
            sublist = StatoSala.Tavoli[self.contatore:lenght]
            for tavolo in sublist:
                self.layout.addWidget(BlockTavolo(tavolo))
                self.contatore += 1




