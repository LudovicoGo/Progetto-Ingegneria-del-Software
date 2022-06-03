from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout,QListWidget,QListWidgetItem, QHBoxLayout, QLabel,QLineEdit, QSizePolicy
from RistoMatic.GestioneAttivita.Comanda import Comanda
from RistoMatic.GestioneAttivita.Tavolo import Tavolo

class BlockComandaSala(QtWidgets.QGroupBox):

    def __init__(self, comanda: Comanda):
        if (isinstance(comanda.rif, Tavolo)):
            super().__init__(
                f"Comanda {comanda.numeroComanda} - Tavolo {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
        else:
            super().__init__(
                f"Comanda {comanda.numeroComanda} - Asporto {comanda.rif.riferimentoTavolo} - {comanda.dataCreazione.strftime('%H:%M')}")
            self.setStyleSheet("QGroupBox {background-color: blue;}")

        self.setMinimumWidth(300)
        self.comanda=comanda

        self.vbox = QVBoxLayout()
        #self.vbox.addWidget(self.btntavolo)
        self.vbox.addStretch(1)

        for elemento in comanda.elementiComanda:
            info = elemento.getInfoElementoComanda()

            col1 = QVBoxLayout()
            elem = QLabel(info["Nome"])
            elem.setStyleSheet("QLabel {font-size: 16px;}")
            col1.addWidget(elem)
            col1.addWidget(QLabel(info["Note"]))

            col2 = QVBoxLayout()
            col2.addWidget(QLabel(f"Qty"))
            line = QLineEdit()
            line.setFixedSize(25,25)
            line.setText(str(info["Quantita"]))
            line.setStyleSheet("QLineEdit {width: 3;}")
            col2.addWidget(line)

            col3 = QVBoxLayout()
            btnp =QPushButton("+")
            btnp.setFixedSize(25,25)
            col3.addWidget(btnp)
            btnm = QPushButton("-")
            btnm.setFixedSize(25,25)
            col3.addWidget(btnm)

            col4 = QVBoxLayout()
            col4.addWidget(QLabel(str(info["Prezzo"])))
            col4.addWidget(QLabel(str(info["Prezzo"]*info["Quantita"])))
            col4.setAlignment(Qt.AlignRight)
            row = QHBoxLayout()
            row.addLayout(col1)
            row.addLayout(col2)
            row.addLayout(col3)
            row.addLayout(col4)

            self.vbox.addLayout(row)

        tot = QHBoxLayout()
        tot.addWidget(QLabel("Totale: "+ str(comanda.getTotale()) +" €"))
        self.vbox.addLayout(tot)
        self.setLayout(self.vbox)