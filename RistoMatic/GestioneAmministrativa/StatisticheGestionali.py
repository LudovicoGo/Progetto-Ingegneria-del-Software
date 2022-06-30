import datetime
import pickle

import pandas
from RistoMatic.GestioneAmministrativa.Statistiche import Statistiche
from RistoMatic.GestioneAttivita import StatoSala

class StatisticheGestionali(Statistiche):

    def __init__(self, dataInizio , dataFine):
        super().__init__(dataInizio,dataFine)



    # Media ORDINI ASPORTO , ORDINI TAVOLI
    # Totale ORDINI ASPORTO , ORDINI TAVOLI

    # Restituisce due dizionari con la seguente sintassi: dict = { data : lista_comande , ... }
    def calcolaStatistiche(self):

         if ( self.dataInizio is None) or (self.dataFine is None) :
              self.dataFine = datetime.date.today()
              self.dataInizio = datetime.datetime.today() - datetime.timedelta(days=1)


         storicoComande = []
         with (open("Dati/Comande.pickle", "rb")) as openfile:
           while True:
             try:
                storicoComande = pickle.load(openfile)
             except EOFError:
                 break

         inizio = datetime.date(self.dataInizio.year,self.dataInizio.month,self.dataInizio.day)
         fine = datetime.date(self.dataFine.year,self.dataFine.month,self.dataFine.day)
         date_list = pandas.date_range(start=inizio,end=fine)
         # per ogni giorno controllo controllo l'incasso
         OrdiniAsporto = {}
         OrdiniTavolo = {}
         for data in date_list:
            comandeAsporto = []
            comandeTavolo = []
            for comanda in storicoComande:
                dataComanda = datetime.date(comanda.dataCreazione.year,comanda.dataCreazione.month,comanda.dataCreazione.day)
                if dataComanda == datetime.date(data.year,data.month,data.day):
                    if comanda.isAsporto() is True:
                        comandeAsporto.append(comanda)
                    elif comanda.isTavolo() is True:
                        comandeAsporto.append(comanda)
            OrdiniAsporto[datetime.date(data.year,data.month,data.day)] = comandeAsporto
            OrdiniTavolo[datetime.date(data.year,data.month,data.day)] = comandeTavolo
         print('Ordini Asporto: ' , OrdiniAsporto)
         print('Ordini Tavolo: ' , OrdiniTavolo)

         return (OrdiniAsporto , OrdiniTavolo)







#   TODO LUCA : Vedere perchè non mi tratta i dizionari come tali(OrdineAsporto , OrdineTavolo)
#   Posso avere statistiche come segue: giorno con piu ordini , giorno con meno ordini , media ordini nel periodo di tempo
#   Quante bevande / pietanze si sono presi in quei giorni
    def generaStatistiche(self)->dict:
        datiRaffinati = {}
        OrdiniAsporto , OrdiniTavolo = self.calcolaStatistiche()
        pass






        
        


