from PySide6.QtCore import Slot, Signal
from PySide6 import QtWidgets
from random import *
from RistoMatic.Viste.FlowLayout import FlowLayout
from RistoMatic.Viste.Blocks.BlockTavolo import BlockTavolo
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Tavolo import Tavolo


class VistaMobile(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.layout = FlowLayout(self)
        for tavolo in StatoSala.Tavoli:
            btn = BlockTavolo(tavolo)
            # btn.update_ui.connect(self.aggiungi)
            self.layout.addWidget(btn)

    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        for tavolo in StatoSala.Tavoli:
            btn = BlockTavolo(tavolo.numero, tavolo.stat)
            btn.update_ui.connect(self.aggiungi)
            self.layout.addWidget(btn)
