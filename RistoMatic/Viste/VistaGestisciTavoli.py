from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QListView, QComboBox


class VistaGestisciTavoli(QtWidgets.QWidget):

# definire qualcosa per la callback
    def __init__(self):
        super().__init__()

        self.aggiorna()

        self.buttonsLayout = QHBoxLayout()
        self.vLayout = QVBoxLayout()

        self.aggiungiTavolo = QPushButton('Aggiungi Tavolo')
        self.aggiungiTavolo.clicked.connect(self.addTavolo)

        self.eliminaTavolo= QPushButton('Elimina Tavolo')
        self.eliminaTavolo.clicked.connect(self.deleteTavolo)

        self.sceltaPosti = QComboBox()
        posti = [str(i) for i in range(1,51)]
        self.sceltaPosti.addItems(posti)

        self.buttonsLayout.addWidget(self.aggiungiTavolo)
        self.buttonsLayout.addWidget(self.eliminaTavolo)
        self.vLayout.addWidget(self.sceltaPosti)

        self.vLayout.addLayout(self.buttonsLayout)

        self.listView = QListView()
        self.vLayout.addWidget(self.listView)

        self.setLayout(self.vLayout)




#  Clicco con il mouse su crea tavolo e dopo ne aggiungo uno nuovo
    def addTavolo(self):
        pass



#  Clicco sul tavolo con il mouse e dopo lo rimuovo
    def deleteTavolo(self):
        pass

#  Aggiorna la vista dopo che abbiamo lavorato con i tavoli ,ad esempio se vengono aggiunti o rimossi i tavoli, il metodo
#  viene chiamato e richiama alla fine se-stesso
    def aggiorna(self):
        pass

