from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QListView
from PySide6.examples.widgets.layouts.flowlayout.flowlayout import FlowLayout

from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.Viste.ClasseTestLudovico import ClasseTestLudovico
from RistoMatic.Viste.Blocks.BlockComandaAsporto import BlockComandaAsporto
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer

from RistoMatic.Viste.Blocks.BlockComandaSala import BlockComandaSala
from RistoMatic.Viste.FlowLayout import FlowLayout

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from random import *

class VistaAsporto(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = FlowLayout(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.aggiorna)
        self.timer.start(5000)
        self.lista = ClasseTestLudovico()
        #for comanda in StatoSala.getListaAsporto():
        self.addButton = QPushButton("Aggiungi nuovo ordine")
        self.addButton.clicked.connect(self.aggiungiNuovoOrdine)
        self.layout.addWidget(self.addButton)
        for ordine in StatoSala.getListaAsporto(self):
            self.layout.addWidget(BlockComandaAsporto(ordine))

    def aggiorna(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        for ordine in StatoSala.getListaAsporto(self):
#            self.bb = QPushButton('bottone')
#            self.addButton.clicked.connect(self.pas)
#            self.layout.addWidget(self.bb)
            self.layout.addWidget(BlockComandaAsporto(ordine))

    def aggiungiNuovoOrdine(self):
        print('Aggiungi Ordine')
        self.cliente = Cliente('Albertino', '987654321')
        ooordine = OrdineAsporto('21:00', '19:30', self.cliente)
        e = ElementoMenu("pizza", "bar", 12)
        a = ElementoComanda(e, "nessuna", 12)
        ooordine.comanda.elementiComanda.append(a)
        StatoSala.OrdiniAsporto.append(ooordine)

    def pas(self):
        pass