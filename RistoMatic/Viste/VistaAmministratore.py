import datetime
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QListView, QMessageBox,QApplication, QDialog
# TODO LUCA : Risolvere problema import VistaGrafico
from RistoMatic.Viste.VistaGrafico import VistaGrafico
from RistoMatic.GestioneAmministrativa.StatisticheEconomiche import StatisticheEconomiche
from RistoMatic.GestioneAmministrativa.StatisticheGestionali import StatisticheGestionali
from RistoMatic.GestioneAmministrativa.StatisticheGestionali import Statistiche
import datetime

from PySide6.QtWidgets import QApplication, QWidget, QCalendarWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QDateTimeEdit, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QTextCharFormat, QIcon

import pandas as pd


# Aggiunto Qwidget
class vistaCalendario(QCalendarWidget):
    def __init__(self):
        super().__init__()

        self.from_date = None
        self.to_date = None

        self.highlighter_format = QTextCharFormat()
        # get the calendar default highlight setting
        self.highlighter_format.setBackground(self.palette().brush(QPalette.Highlight))
        self.highlighter_format.setForeground(self.palette().color(QPalette.HighlightedText))

        # this will pass selected date value as a QDate object
        self.clicked.connect(self.select_range)

        super().dateTextFormat()

    def highlight_range(self, format):
        if self.from_date and self.to_date:
            d1 = min(self.from_date, self.to_date)
            d2 = max(self.from_date, self.to_date)
            while d1 <= d2:
                self.setDateTextFormat(d1, format)
                d1 = d1.addDays(1)

    def select_range(self, date_value):
        self.highlight_range(QTextCharFormat())

        # check if a keyboard modifer is pressed
        if QApplication.instance().keyboardModifiers() & Qt.ShiftModifier and self.from_date:
            self.to_date = date_value
            # print(self.from_date, self.to_date)
            self.highlight_range(self.highlighter_format)
        else:
            # required
            self.from_date = date_value
            self.to_date = None
        # print(self.from_date, self.to_date, 'x')

    def acquisizioneGiorni(self):



        global start_date, end_date
        if self.from_date and self.to_date:
        # Devo lavorare con i datetime , quindi estrapolo manualmente anni , mesi e giorni e creo un nuovo oggetto datetime
            toAnno = self.to_date.year()
            toMese = self.to_date.month()
            toGiorno = self.to_date.day()
            toData = datetime.datetime(toAnno,toMese,toGiorno)

            fromAnno = self.from_date.year()
            fromMese = self.from_date.month()
            fromGiorno = self.from_date.day()
            fromData = datetime.datetime(fromAnno,fromMese,fromGiorno)

            # print(self.calendar.to_date.toPyDate.strftime("%Y-%m-%d"))
            start_date = min(toData, fromData)
            end_date = max(toData, fromData)

            # print('Number of days: {0}'.format((end_date - start_date).days))
            date_list = pd.date_range(start=start_date, end=end_date)
           # print(date_list)


        try:
            return start_date , end_date
        except:
              return None



## FINE APP

from RistoMatic.Viste.VistaUnlockAmministratore import VistaUnlockAmministratore
class VistaAmministratore(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()
#       Serve per fare il login

        hLayout = QHBoxLayout()

        self.listView = QListView()
        hLayout.addWidget(self.listView)

        buttonsLayout = QVBoxLayout()

        global newButton1
        self.statistiche = None
        newButton1 = QPushButton("Salva statistiche")
        newButton1.setEnabled(False)
        newButton1.clicked.connect(self.salvaStatistiche)

        global infoButton
        infoButton = QPushButton("Genera Statistiche Economiche")
        infoButton.clicked.connect(self.statisticheEconomiche)

        global newButton
        newButton = QPushButton("Genera Statistiche Gestionali")
        newButton.clicked.connect(self.statisticheGestionali)

        annullaButton = QPushButton('Reset')
        annullaButton.clicked.connect(self.reset)

        buttonsLayout.addWidget(newButton1)
        buttonsLayout.addWidget(newButton)
        buttonsLayout.addWidget(infoButton)
        buttonsLayout.addWidget(annullaButton)

        hLayout.addLayout(buttonsLayout)

        self.setLayout(hLayout)
        self.resize(600, 300)
        self.setWindowTitle("Amministrazione")




        ###      AGGIUNTA vistaCalendario CON SCELTA MULTIPLA   ###

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        # IL PROBLEMA STA IN QUESTA RIGA DI CODICE
        self.calendar = vistaCalendario()  # IL PROBLEMA STA IN QUESTA RIGA DI CODICE
        self.layout.addWidget(self.calendar)
        hLayout.addLayout(self.layout)

        #btn = QPushButton('Conferma filtro')

       # btn.clicked.connect(self.calendar.acquisizioneGiorni)
        #self.layout.addWidget(btn)


    def salvaStatistiche(self):
        if(self.statistiche is None) : return
        self.statistiche.esportaStatistiche()
        msg = QMessageBox()
        msg.setWindowTitle('Statistiche RistoMatic')
        msg.setText("SUCCESSO !")
        msg.setInformativeText("Statistica salvata corretamente, prego controlla nella cartella ./Dati")
        msg.exec_()
        newButton1.setEnabled(False)
        infoButton.setEnabled(True)
        newButton.setEnabled(True)




    def statisticheEconomiche(self):
        vistaGrafico = VistaGrafico()

        if self.calendar.acquisizioneGiorni() is None :
          # Non ho inserito , nulla, avro i campi del costruttore di genera statistiche economiche vuoto
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Attenzione!")
          msg.setInformativeText("Non hai inserito nessun range di date, per convenzione verranno prese le ultime 24 ore !")
          msg.exec_()
          self.statistiche = StatisticheEconomiche(None,None)
          newButton1.setEnabled(True)
          newButton.setEnabled(False)
          vistaGrafico.graficoStatisticheEconomiche(self.statistiche.calcolaStatistiche())
        else:
            start,end=self.calendar.acquisizioneGiorni()

            if(datetime.date(end.year,end.month,end.day)>datetime.date.today() or datetime.date(start.year,start.month,start.day)==datetime.date(end.year,end.month,end.day)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Attenzione al range di date selezionate !")
                msg.exec_()
                return
            # Range di dati validi:
            else:
                self.statistiche = StatisticheEconomiche(start,end)
                newButton1.setEnabled(True)
                newButton.setEnabled(False)
                vistaGrafico.graficoStatisticheEconomiche(self.statistiche.calcolaStatistiche())
                #newButton1.clicked.connect(self.salvaStatistiche(statistiche))
                #print('Tipo oggetto: vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche) : ' ,type(vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche)))
                #print('Tipo oggetto statistiche.calcolaStatistiche()' , type(statistiche.calcolaStatistiche()))
                #vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
                #print(statistiche.generaStatistiche())






    def statisticheGestionali(self):

        vistaGrafico = VistaGrafico()

        if self.calendar.acquisizioneGiorni() is None :
          # Non ho inserito , nulla, avro i campi del costruttore di genera statistiche economiche vuoto
          msg = QMessageBox()
          msg.setIcon(QMessageBox.Critical)
          msg.setText("Attenzione!")
          msg.setInformativeText("Non hai inserito nessun range di date, per convenzione verranno prese le ultime 24 ore !")
          msg.exec_()
          self.statistiche = StatisticheGestionali(None,None)
          ordiniAsporto,ordiniTavolo = self.statistiche.calcolaStatistiche()
          vistaGrafico.graficoStatisticheGestionali(ordiniAsporto,ordiniTavolo)
          newButton1.setEnabled(True)
          infoButton.setEnabled(False)
          #print(statistiche.generaStatistiche())
         # vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
        else:
            start,end=self.calendar.acquisizioneGiorni()

            if(datetime.date(end.year,end.month,end.day)>datetime.date.today() or datetime.date(start.year,start.month,start.day)==datetime.date(end.year,end.month,end.day)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Attenzione al range di date selezionate !")
                msg.exec_()
                return
            # Range di dati validi:
            else:
                self.statistiche = StatisticheGestionali(start,end)
                ordiniAsporto,ordiniTavolo = self.statistiche.calcolaStatistiche()
                vistaGrafico.graficoStatisticheGestionali(ordiniAsporto,ordiniTavolo)
                newButton1.setEnabled(True)
                infoButton.setEnabled(False)
                #print('ORDINI ASPORTO: ', a)
                #print('ORDINI TAVOLO: ', b)
                #print('Tipo oggetto: vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche) : ' ,type(vistaGrafico.graficoStatisticheEconomiche(self,statistiche.calcolaStatistiche)))
                #print('Tipo oggetto statistiche.calcolaStatistiche()' , type(statistiche.calcolaStatistiche()))
                #vistaGrafico.graficoStatisticheEconomiche(statistiche.calcolaStatistiche())
                #print(statistiche.generaStatistiche())




    def reset(self):
        newButton1.setEnabled(False)
        infoButton.setEnabled(True)
        newButton.setEnabled(True)

