import datetime
import pickle
from RistoMatic.GestioneAmministrativa.Statistiche import Statistiche


class StatisticheGestionali(Statistiche):

    def __init__(self, dataInizio , dataFine):
        super.__init__(dataInizio,dataFine)


    def __init__(self):
        super.__init__()


    # Media ORDINI ASPORTO , ORDINI TAVOLI
    # Totale ORDINI ASPORTO , ORDINI TAVOLI


    def calcolaStatistiche(self)->dict:
         datiGrezzi = {}

         if ( self.dataInizio is None) or (self.dataFine is None) :
              self.dataFine = datetime.date.today()
              self.dataInizio = datetime.datetime.today() - datetime.timedelta(days=1)


         with (open("Comande.pickle", "rb")) as openfile:
           while True:
             try:
                storicoComande = pickle.load(openfile)
             except EOFError:
                 break

         OrdiniAsporto = {}
         OrdiniTavolo = {}
         for comanda in storicoComande:
#   Attenzione nel dizionario ci sarà come valore una lista di elementi , tenerne conto !
           if comanda.isAsporto:
             OrdiniAsporto.pop(comanda.dataCreazione,comanda.elementiComanda)
           elif comanda.isTavolo:
               OrdiniTavolo.pop(comanda.dataCreazione,comanda.elementiComanda)
               
         return OrdiniAsporto , OrdiniTavolo


#   TODO LUCA : Vedere perchè non mi tratta i dizionari come tali(OrdineAsporto , OrdineTavolo)
#   Posso avere statistiche come segue: giorno con piu ordini , giorno con meno ordini , media ordini nel periodo di tempo
#   Quante bevande / pietanze si sono presi in quei giorni
    def generaStatistiche(self)->dict:
        datiRaffinati = {}
        OrdiniAsporto , OrdiniTavolo = self.calcolaStatistiche()
        pass






        
        


