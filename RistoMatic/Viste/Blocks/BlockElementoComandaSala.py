from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout,QListWidget,QListWidgetItem, QHBoxLayout, QLabel,QLineEdit
from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.Viste.Blocks.LineSeparator import QHSeperationLine


class BlockElementoComandaSala(QtWidgets.QVBoxLayout):

    aggiorna_comanda = Signal()

    def __init__(self, elemento: ElementoComanda):
        super().__init__()
        self.elemento = elemento

        info = self.elemento.getInfoElementoComanda()

        self.col1 = QVBoxLayout()
        self.elem = QLabel(info["Nome"])
        self.elem.setStyleSheet("QLabel {font-size: 16px;}")
        self.col1.addWidget(self.elem)
        self.col1.addWidget(QLabel(info["Note"]))

        self.col2 = QVBoxLayout()
        self.col2.addWidget(QLabel(f"Qty"))
        self.box = QLineEdit()
        self.box.setFixedSize(25,25)
        self.box.setText(str(info["Quantita"]))
        self.box.setStyleSheet("QLineEdit {width: 3;}")
        self.col2.addWidget(self.box)

        self.col3 = QVBoxLayout()
        self.btnp =QPushButton("+")
        self.btnp.clicked.connect(self.aggiungi)
        self.btnp.setFixedSize(25,25)
        self.col3.addWidget(self.btnp)
        self.btnm = QPushButton("-")
        self.btnm.clicked.connect(self.rimuovi)
        self.btnm.setFixedSize(25,25)
        self.col3.addWidget(self.btnm)

        self.col4 = QVBoxLayout()
        self.col4.addWidget(QLabel(str(info["Prezzo"])))
        self.prezzo= QLabel(str(info["Prezzo"]*info["Quantita"]))
        self.col4.addWidget(self.prezzo)
        self.col4.setAlignment(Qt.AlignRight)
        self.row = QHBoxLayout()
        self.row.setAlignment(Qt.AlignTop)
        self.row.addLayout(self.col1)
        self.row.addLayout(self.col2)
        self.row.addLayout(self.col3)
        self.row.addLayout(self.col4)

        self.line = QVBoxLayout()
        self.line.setAlignment(Qt.AlignTop)
        self.line.addLayout(self.row)
        self.line.addWidget(QHSeperationLine())

        self.addLayout(self.line)

    def aggiungi(self):
        self.elemento.setQuantita(self.elemento.getQuantita() +1)
        self.box.setText(str(self.elemento.getQuantita()))
        info = self.elemento.getInfoElementoComanda()
        self.prezzo.setText(str(info["Prezzo"]*info["Quantita"]))
        self.aggiorna_comanda.emit()

    def rimuovi(self):
        val = (self.elemento.getQuantita() -1)
        if val >0:
            self.elemento.setQuantita(val)
            self.box.setText(str(self.elemento.getQuantita()))
            info = self.elemento.getInfoElementoComanda()
            self.prezzo.setText(str(info["Prezzo"] * info["Quantita"]))
            self.aggiorna_comanda.emit()

