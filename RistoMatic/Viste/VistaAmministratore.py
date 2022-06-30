import datetime

from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QListView, QMessageBox

# TODO LUCA : Risolvere problema import VistaGrafico

from RistoMatic.GestioneAmministrativa.StatisticheEconomiche import StatisticheEconomiche
from RistoMatic.GestioneAmministrativa.StatisticheGestionali import StatisticheGestionali
from RistoMatic.GestioneAmministrativa.StatisticheGestionali import Statistiche
from RistoMatic.Utility.Calendario import Calendario
#from RistoMatic.Viste.VistaGrafico import VistaGrafico

class VistaAmministratore(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()
        hLayout = QHBoxLayout()

        self.listView = QListView()
        hLayout.addWidget(self.listView)

        buttonsLayout = QVBoxLayout()

        global newButton1
        newButton1 = QPushButton("Salva statistiche")
        newButton1.setEnabled(False)
        print('newButton1 status iniziale : ' , newButton1.clicked)


        infoButton = QPushButton("Genera Statistiche Economiche")
        infoButton.clicked.connect(self.statisticheEconomiche)

        newButton = QPushButton("Genera Statistiche Gestionali")
        newButton.clicked.connect(self.statisticheGestionali)

        buttonsLayout.addWidget(newButton1)
        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(infoButton)

        hLayout.addLayout(buttonsLayout)

        self.setLayout(hLayout)
        self.resize(600, 300)
        self.setWindowTitle("Amministrazione")




        ###      AGGIUNTA CALENDARIO CON SCELTA MULTIPLA   ###

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        # IL PROBLEMA STA IN QUESTA RIGA DI CODICE
        self.calendar = Calendario()  # IL PROBLEMA STA IN QUESTA RIGA DI CODICE
        self.layout.addWidget(self.calendar)
        hLayout.addLayout(self.layout)

        #btn = QPushButton('Conferma filtro')

       # btn.clicked.connect(self.calendar.print_days_selected)
        #self.layout.addWidget(btn)


    def salvaStatistiche(self, statistiche : Statistiche):
        print('Il pulsante è stato cliccato')
        statistiche.esportaStatistiche()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("SUCCESSO !")
        msg.setInformativeText("Statistica salvata corretamente, prego controlla nella cartella ./Dati")
        msg.exec_()






    def statisticheEconomiche(self):

        #vistaGrafico = VistaGrafico()

        if self.calendar.print_days_selected() is None :
          # Non ho inserito , nulla, avro i campi del costruttore di genera statistiche economiche vuoto
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Attenzione!")
          msg.setInformativeText("Non hai inserito nessun range di date, per convenzione verranno prese le ultime 24 ore !")
          msg.exec_()
          statistiche = StatisticheEconomiche(None,None)
        #newButton1.clicked.connect(self.salvaStatistiche)
          #print(statistiche.generaStatistiche())
          #vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
        else:
            start,end=self.calendar.print_days_selected()

            if(datetime.date(end.year,end.month,end.day)>datetime.date.today() or datetime.date(start.year,start.month,start.day)==datetime.date(end.year,end.month,end.day)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Attenzione al range di date selezionate !")
                msg.exec_()
                return
            # Range di dati validi:
            else:
                statistiche = StatisticheEconomiche(start,end)
                newButton1.setEnabled(True)
                print('newButton1 status finale: ' , newButton1.clicked)
                newButton1.clicked.connect(self.salvaStatistiche(statistiche))
                #print('Tipo oggetto: vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche) : ' ,type(vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche)))
                #print('Tipo oggetto statistiche.calcolaStatistiche()' , type(statistiche.calcolaStatistiche()))
                #vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
                #print(statistiche.generaStatistiche())






    def statisticheGestionali(self):

        #vistaGrafico = VistaGrafico()

        if self.calendar.print_days_selected() is None :
          # Non ho inserito , nulla, avro i campi del costruttore di genera statistiche economiche vuoto
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Attenzione!")
          msg.setInformativeText("Non hai inserito nessun range di date, per convenzione verranno prese le ultime 24 ore !")
          msg.exec_()
          statistiche = StatisticheGestionali(None,None)
          #print(statistiche.generaStatistiche())
         # vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
        else:
            start,end=self.calendar.print_days_selected()

            if(datetime.date(end.year,end.month,end.day)>datetime.date.today() or datetime.date(start.year,start.month,start.day)==datetime.date(end.year,end.month,end.day)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Attenzione al range di date selezionate !")
                msg.exec_()
                return
            # Range di dati validi:
            else:
                statistiche = StatisticheGestionali(start,end)
                a,b = statistiche.calcolaStatistiche()

                print(a)
                #print('ORDINI ASPORTO: ', a)
                #print('ORDINI TAVOLO: ', b)
                #print('Tipo oggetto: vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche) : ' ,type(vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche)))
                #print('Tipo oggetto statistiche.calcolaStatistiche()' , type(statistiche.calcolaStatistiche()))
                #vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
                #print(statistiche.generaStatistiche())
        pass
