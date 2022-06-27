from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QListView,  QCalendarWidget

from RistoMatic.Utility.Calendario import Calendario
from RistoMatic.Viste.FlowLayout import FlowLayout
from RistoMatic.Viste.VistaFiltroStatistiche import VistaFiltroStatistiche
import pandas as pd


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
        btn = QPushButton('Retrieve Date Range', clicked=self.print_days_selected)
        self.layout.addWidget(btn)

        self.calendar = Calendario()  # IL PROBLEMA STA IN QUESTA RIGA DI CODICE

        self.layout.addWidget(self.calendar)
        hLayout.addLayout(self.layout)

    def print_days_selected(self, calendar):
        #PROBLEMA NON ENTRA QUI DENTRO
        if  calendar.from_date and calendar.to_date:
            start_date = min(self.calendar.from_date.toPyDate(), self.calendar.to_date.toPyDate())
            end_date = max(self.calendar.from_date.toPyDate(), self.calendar.to_date.toPyDate())
            # print('Number of days: {0}'.format((end_date - start_date).days))
            date_list = pd.date_range(start=start_date, end=end_date)
            print(date_list)

        else:
            print('No date range is selected')


    ###     FINE CALENDARIO SCELTA MULTIPLA    ###

    def statisticheEconomiche(self):
        pass

    def statisticheGestionali(self):
        pass
