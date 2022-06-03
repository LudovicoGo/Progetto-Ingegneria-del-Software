from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from RistoMatic.Viste.FlowLayout import FlowLayout
from RistoMatic.Viste.Blocks.BlockComandaPreparazione import BlockComandaPreparazione
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAttivita.Enum import StatoComanda
from random import *

class VistaPreparazione(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # generazione dati di esempio
        for i in range(0, 10):
            tavolo = Tavolo(randint(1, 10))
            comanda = Comanda(tavolo)
            comanda.elementiComanda.append(ElementoComanda(ElementoMenu("asd", "", 2),"nota",2))
            comanda.elementiComanda.append(ElementoComanda(ElementoMenu("asddd", "", 22), "", 1))
            StatoSala.Comande.append(comanda)
            StatoSala.Tavoli.append(tavolo)

        self.layout = FlowLayout(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.aggiorna)
        self.timer.start(5000)

        for comanda in StatoSala.Comande:
            self.layout.addWidget(BlockComandaPreparazione(comanda))

    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        for comanda in StatoSala.Comande:
            if not comanda.getStato()==StatoComanda.COMPLETATA:
                self.layout.addWidget(BlockComandaPreparazione(comanda))