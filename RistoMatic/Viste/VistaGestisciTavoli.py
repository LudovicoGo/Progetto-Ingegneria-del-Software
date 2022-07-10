from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QPushButton, QSizePolicy, QHBoxLayout, QListView, QVBoxLayout
from PySide6 import QtWidgets

from RistoMatic.GestioneAttivita.StatoSala import StatoSala


class VistaGestisciTavoli(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        hLayout = QHBoxLayout()

    #    self.aggiorna = QTimer()
    #    self.aggiorna.setInterval(5000)
    #    self.aggiorna.timeout.connect(self.aggiornaUi)
    #    self.aggiorna.start()

        self.listView = QListView()
        self.aggiornaUi()
        hLayout.addWidget(self.listView)

        buttonsLayout = QVBoxLayout()
        infoButton = QPushButton("Tasto 1")
        infoButton.clicked.connect(self.visualizzaAltreInformazioni)

        newButton = QPushButton("Crea nuovo tavolo")
        newButton.clicked.connect(self.nuovoTavolo)

        delButton = QPushButton("Elimina tavolo selezionato")
        delButton.clicked.connect(self.eliminaTavolo)

        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(infoButton)
        buttonsLayout.addWidget(delButton)

        buttonsLayout.addStretch()
        hLayout.addLayout(buttonsLayout)

        self.setLayout(hLayout)
        self.resize(600, 300)
        self.setWindowTitle("Gestione tavoli")

    def nuovoTavolo(self):
        print('nuovoTavolo')

    def eliminaTavolo(self):
        print('eliminaTavolo')

    def visualizzaAltreInformazioni(self):
        print('VisualizzaAltreInformazioni')


    def aggiornaUi(self):
        listViewModel = QStandardItemModel(self.listView)
#        StatoSala.Tavoli.sort()

        for tavolo in StatoSala.Tavoli:  # mostra le infromazioni del tavolo per ogni tavolo nella lista Tavoli in stato sala
            qItem = QStandardItem()

            titolo = f"Numero tavolo: {tavolo.riferimentoTavolo}, Numero posti massimo: {tavolo.numeroPosti}"
            qItem.setText(titolo)
            qItem.setEditable(False)
            font = qItem.font()
            font.setPointSize(20)
            qItem.setFont(font)
            listViewModel.appendRow(qItem)

        self.listView.setModel(listViewModel)

    def getGenericButton(self, titolo, onClick):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(onClick)
        return
