from PySide6.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QListView

from PySide6 import QtWidgets


class VistaGestisciMenu(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.buttonsLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()

        self.aggiungiMenu = QPushButton('Aggiungi menù')
        self.aggiungiMenu.clicked.connect(self.addMenu)

        self.eliminaMenu = QPushButton('Elimina menù')
        self.eliminaMenu.clicked.connect(self.deleteMenu)

        self.buttonsLayout.addWidget(self.aggiungiMenu)
        self.buttonsLayout.addWidget(self.eliminaMenu)
        self.vLayout.addLayout(self.buttonsLayout)

        self.listView = QListView()
        self.vLayout.addWidget(self.listView)

        self.setLayout(self.vLayout)
        #self.resize(600, 300)


    def addMenu(self):
        print('addMenu')


    def deleteMenu(self):
        print('deleteMenu')




