from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QListView

from RistoMatic.Viste.FlowLayout import FlowLayout
from RistoMatic.Viste.VistaFiltroStatistiche import VistaFiltroStatistiche


class VistaAmministratore(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        hLayout = QHBoxLayout()


        self.listView = QListView()
        hLayout.addWidget(self.listView)

        buttonsLayout = QVBoxLayout()

        infoButton = QPushButton("Genera Statistiche Economiche")
        infoButton.clicked.connect(self.statisticheEconomiche)

        newButton = QPushButton("Genera Statistiche Gestionali")
        newButton.clicked.connect(self.statisticheGestionali)

        newButton1 = QPushButton("Esporta e salva statistiche")
        newButton.clicked.connect(self.statisticheGestionali)



        buttonsLayout.addWidget(newButton1)
        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(infoButton)

        hLayout.addLayout(buttonsLayout)

        self.setLayout(hLayout)
        self.resize(600, 300)
        self.setWindowTitle("Amministrazione")



        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(infoButton)

        buttonsLayout.addStretch()
        hLayout.addLayout(buttonsLayout)

#        self.layout().addWidget()



    def statisticheEconomiche(self):
        self.inserisciPrenotazione = VistaFiltroStatistiche()
        prenotazione = self.inserisciPrenotazione.show()
    def statisticheGestionali(self):
        pass
