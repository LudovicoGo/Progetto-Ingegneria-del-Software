from PySide6.QtCore import Slot,Signal

from Viste.FlowLayout import FlowLayout
from random import *
from Viste.Blocks.BlockTavolo import BlockTavolo
from Model.StatoSala import StatoSala
from PySide6 import QtWidgets
from Model.Tavolo import Tavolo

class VistaMobile(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()

        self.layout = FlowLayout(self)
        for tavolo in StatoSala.Tavoli:
            btn=BlockTavolo(tavolo.numero, tavolo.stat)
            btn.update_ui.connect(self.aggiungi)
            self.layout.addWidget(btn)

    @Slot()
    def aggiungi(self):
        tavolo = Tavolo(99,"Libero")
        tavolo.aggiungitavolo()
        self.aggiorna()

    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        for tavolo in StatoSala.Tavoli:
            btn = BlockTavolo(tavolo.numero, tavolo.stat)
            btn.update_ui.connect(self.aggiungi)
            self.layout.addWidget(btn)

