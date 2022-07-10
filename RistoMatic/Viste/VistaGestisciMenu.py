from PySide6.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QListView

from PySide6 import QtWidgets

from RistoMatic.Viste.VistaAggiungiMenu import VistaAggiungiMenu


class VistaGestisciMenu(QtWidgets.QWidget):

# definire qualcosa per la callback
    def __init__(self):
        super().__init__()

        self.aggiorna()

        self.buttonsLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()

        self.aggiungiMenu = QPushButton('Aggiungi menù')
        self.aggiungiMenu.clicked.connect(self.addMenu)

        self.eliminaMenu = QPushButton('Elimina menù')
        self.eliminaMenu.clicked.connect(self.deleteMenu)

        self.scegliMenu = QPushButton('Menu per la serata')
        self.scegliMenu.clicked.connect(self.selectMenu)

        self.modificaMenu = QPushButton('Modifica menu')
        self.modificaMenu.clicked.connect(self.updateMenu)

        self.buttonsLayout.addWidget(self.aggiungiMenu)
        self.buttonsLayout.addWidget(self.eliminaMenu)
        self.buttonsLayout.addWidget(self.scegliMenu)
        self.buttonsLayout.addWidget(self.modificaMenu)
        self.vLayout.addLayout(self.buttonsLayout)

        self.listView = QListView()
        self.vLayout.addWidget(self.listView)

        self.setLayout(self.vLayout)
        #self.resize(600, 300)



#  Clicco sul menu con il mouse e dopo ne aggiungo uno nuovo
    def addMenu(self):
        self.vistaAggiungiMenu = VistaAggiungiMenu()
        self.vistaAggiungiMenu.setWindowTitle('Menù')
        self.vistaAggiungiMenu.show()


#  Clicco sul menu con il mouse e dopo lo rimuovo
    def deleteMenu(self):
        pass


# Clicco su menù con il mouse e dopo lo seleziono come predefinito per la serata
    def selectMenu(self):
        pass


# Clicco sul menù con il mouse e dopo premendo il pulsante AGGIORNA , lo vado a modificare
    def updateMenu(self):
        pass


#  Aggiorna la vista dopo che abbiamo lavorato con i menu ,ad esempio se vengono aggiunti o rimossi i menu , il metodo
#  viene chiamato e richiama alla fine se-stesso
    def aggiorna(self):
        pass




