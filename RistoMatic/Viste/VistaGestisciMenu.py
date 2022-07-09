from PySide6.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QListView

# TODO LUCA MODIFICARE E FAR APPARIRE LA VISTA PER GESTIRE I MENU !

class VistaGestisciMenu():

    def __init__(self):
        super.__init__()


        buttonsLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        self.listView = QListView()
        vLayout.addWidget(self.listView)


        aggiungiMenu = QPushButton('Aggiungi menù')
        aggiungiMenu.connect.clicked(self.addMenu)

        eliminaMenu = QPushButton('Elimina menù')
        eliminaMenu.connect.clicked(self.deleteMenu)

        buttonsLayout.addWidget(aggiungiMenu)
        buttonsLayout.addWidget(eliminaMenu)



    def addMenu(self):
        pass


    def deleteMenu(self):
        pass


