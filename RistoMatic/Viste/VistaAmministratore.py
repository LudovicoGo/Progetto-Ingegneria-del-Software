from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QListView, QMessageBox



from RistoMatic.Utility.Calendario import Calendario


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



        print("ECCOMI")
        ###      AGGIUNTA CALENDARIO CON SCELTA MULTIPLA   ###

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        # IL PROBLEMA STA IN QUESTA RIGA DI CODICE
        self.calendar = Calendario()  # IL PROBLEMA STA IN QUESTA RIGA DI CODICE
        self.layout.addWidget(self.calendar)
        hLayout.addLayout(self.layout)


        btn = QPushButton('Conferma filtro')
        btn.clicked.connect(self.calendar.print_days_selected)
        self.layout.addWidget(btn)



    ###     FINE CALENDARIO SCELTA MULTIPLA    ###

    def statisticheEconomiche(self):




    def statisticheGestionali(self):
        pass
