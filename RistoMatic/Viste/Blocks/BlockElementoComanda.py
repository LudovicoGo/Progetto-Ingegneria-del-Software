from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout
from PySide6.QtCore import Slot,Signal

class BlockElementoComanda(QtWidgets.QPushButton):

    remove = Signal()

    def __init__(self, elem, comanda):
        dic = elem.getInfoElementoComanda()
        super().__init__(f"{dic['Quantita']} x {dic['Nome']} \n Nota: {dic['Note']}")

        self.elem = elem
        self.comanda = comanda

        self.clicked.connect(self.contrassegnaElemento)


    def contrassegnaElemento(self):
        self.elem.setIsPronta(True)
        self.deleteLater()