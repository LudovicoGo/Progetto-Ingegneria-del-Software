from PySide6 import QtWidgets
from Viste.FlowLayout import FlowLayout
from Viste.Blocks.BlockComandaPreparazione import BlockComandaPreparazione
from random import *

class VistaPreparazione(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.layout = FlowLayout(self)

        for i in range(0,10):
            self.layout.addWidget(BlockComandaPreparazione(randint(1, 10), randint(0, 100), randint(0, 100)))


    def aggiungi(self, comanda):
        self.layout.addWidget(comanda)
        self.update()

    def rimuovi(self, comanda):
        self.layout.removeWidget(comanda)
        self.update()