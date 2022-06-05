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
        for tavolo in StatoSala.getTavoli():
            self.layout.addWidget(BlockTavolo(tavolo))




