from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGroupBox, QPushButton, QVBoxLayout,QListWidget,QListWidgetItem, QHBoxLayout, QLabel,QLineEdit, QSizePolicy

class BlockComandaSala(QtWidgets.QGroupBox):

    def __init__(self, elements, tavolo, comanda):
        super().__init__()
        self.btntavolo=QPushButton(f"Comanda {comanda} - Tavolo {tavolo}")

        self.setMinimumWidth(300)

        self.comanda=comanda
        self.tavolo=tavolo

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btntavolo)
        self.vbox.addStretch(1)

        self.buttons = []
        for num in range(0,elements):

            col1 = QVBoxLayout()
            elem = QLabel(f"Elemento {num}")
            elem.setStyleSheet("QLabel {font-size: 16px;}")
            col1.addWidget(elem)
            col1.addWidget(QLabel(f"Nota: senza ghiaccio"))

            col2 = QVBoxLayout()
            col2.addWidget(QLabel(f"Qty"))
            line = QLineEdit()
            line.setFixedSize(25,25)
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
            col4.addWidget(QLabel(f"Cad 10"))
            col4.addWidget(QLabel(f"Tot: 30"))
            col4.setAlignment(Qt.AlignRight)
            row = QHBoxLayout()
            row.addLayout(col1)
            row.addLayout(col2)
            row.addLayout(col3)
            row.addLayout(col4)

            self.vbox.addLayout(row)

        self.setLayout(self.vbox)