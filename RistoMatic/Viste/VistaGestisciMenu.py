import pickle

from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QPushButton, QSizePolicy, QHBoxLayout, QListView, QVBoxLayout, QMessageBox
from PySide6 import QtWidgets


from RistoMatic.Viste.VistaAggiungiMenu import VistaAggiungiMenu


class VistaGestisciMenu(QtWidgets.QWidget):

# definire qualcosa per la callback
    def __init__(self):
        super().__init__()

        self.listView = QListView()


        self.buttonsLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()

        self.aggiorna = QTimer()
        self.aggiorna.setInterval(5000)
        self.aggiorna.timeout.connect(self.updateUi)
        self.aggiorna.start()

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

        self.vLayout.addWidget(self.listView)

        self.setLayout(self.vLayout)
        #self.resize(600, 300)




    def updateUi(self):

        listViewModel = QStandardItemModel(self.listView)
        listaMenu = self.readPickleMenu()

        if listaMenu == '' or listaMenu is None :
            print('listaMenu vuota o nulla')
            return

        else:
           for menu in listaMenu:
              qItem = QStandardItem()
#             titolo = f"Nome menu: {menu.nomeMenu}, costo coperto: {menu.costoCoperto}"
              qItem.setText('bbla')
              qItem.setEditable(False)
              font = qItem.font()
              font.setPointSize(20)
              qItem.setFont(font)
              listViewModel.appendRow(qItem)
        self.listView.setModel(listViewModel)



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



#  e se il menu fosse vuoto ?
    def readPickleMenu(self):
        try:
            f = open("Dati/Menu.pickle", "rb")
            storicoMenu = pickle.load(f)
            f.close()
            print(storicoMenu==None)
            return storicoMenu
        except EOFError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Errore lettura del file: Dati/Menu.pickle")
                msg.exec_()
                return




