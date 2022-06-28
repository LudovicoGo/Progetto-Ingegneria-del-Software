import datetime

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

       #todo  luca Fare handling per gestire in caso di scelta sbagliata del range di data
        try:
            inizioCampionamento , fineCampionamento= self.calendar.print_days_selected()
        except:
              msg = QMessageBox()
              msg.setWindowTitle('ATTENZIONE!')
              msg.setIcon(QMessageBox.Critical)
              msg.setText("Errore range data")
              msg.setInformativeText("Sicuro di aver selezionato un range di date?")
              msg.exec_()
              return



    def statisticheEconomiche(self,inizioCampionamento,fineCampionamento):
        if(self.calendar.print_days_selected==None or fineCampionamento>datetime.datetime.now):
            print('erroreeeeee')
            return




    def statisticheGestionali(self):
        pass
