from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QListView, QLineEdit, QLabel

from RistoMatic.Viste.VistaAggiungiElementoMenu import VistaAggiungiElementoMenu


class VistaMenu(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

#       self.hLayout =QHBoxLayout()
        self.vLayout = QVBoxLayout()

        self.listView = QListView()


        self.qlines = {}
#  Ci deve stare il nome del menu quindi : self.addInfoText("nomeMenu" , f"Nome menu: {<NOME_MENU>}")
        self.addInfoText("nomeMenu", "Nome menù: ")

        self.aggiungiElemento = QPushButton('Nuova pietanza')
        self.aggiungiElemento.clicked.connect(self.addElementoMenu)
        self.vLayout.addWidget(self.aggiungiElemento)

        self.eliminaElemento = QPushButton('Elimina pietanza')
        self.eliminaElemento.clicked.connect(self.deleteElementoMenu)
        self.vLayout.addWidget(self.eliminaElemento)

        self.vLayout.addWidget(self.listView)

        self.setLayout(self.vLayout)
#        self.setLayout(self.hLayout)



    def addElementoMenu(self):
        self.vistaAggiungiElementoMenu = VistaAggiungiElementoMenu()
        self.vistaAggiungiElementoMenu.setWindowTitle('Aggiungi pietanza / bevanda')
        self.vistaAggiungiElementoMenu.show()

    def deleteElementoMenu(self):
        pass


    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
#        testo = QLineEdit(self)
 #       self.qlines[nome] = testo
 #       self.vLayout.addWidget(testo)




