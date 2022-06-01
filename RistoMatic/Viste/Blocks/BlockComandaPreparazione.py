from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout

class BlockComandaPreparazione(QtWidgets.QGroupBox):

    def __init__(self, elements, tavolo, comanda):
        super().__init__(f"Comanda {comanda} - Tavolo {tavolo}")

        self.comanda=comanda
        self.tavolo=tavolo

        self.buttons = []
        for num in range(0,elements):
            self.buttons.append(QPushButton(f"Elemento {num} \n Nota: senza ghiaccio"))

        self.vbox = QVBoxLayout()
        for button in self.buttons:
            self.vbox.addWidget(button)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)