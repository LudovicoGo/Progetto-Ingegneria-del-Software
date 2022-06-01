from Viste.FlowLayout import FlowLayout
from random import *
from Viste.Blocks.BlockTavolo import BlockTavolo
from Model.StatoSala import StatoSala
from PySide6 import QtWidgets
from PySide6.QtCore import Signal,Slot, QTimer

class VistaTavoli(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.layout = FlowLayout(self)
        for tavolo in StatoSala.Tavoli:
            self.layout.addWidget(BlockTavolo(tavolo.numero,tavolo.stat))

        self.timer = QTimer()
        self.timer.timeout.connect(self.aggiorna)
        self.timer.start(5000)

    @Slot()
    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        for tavolo in StatoSala.Tavoli:
            self.layout.addWidget(BlockTavolo(tavolo.numero, tavolo.stat))

