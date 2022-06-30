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
    # TODO LUCA VEDERE PER QUALE MOTIVO LA FUNZIONE VIENE RUNNATA DUE VOLTE
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

         return (OrdiniAsporto , OrdiniTavolo)







#   TODO LUCA : Vedere perchè non mi tratta i dizionari come tali(OrdineAsporto , OrdineTavolo)
#   Posso avere statistiche come segue: giorno con piu ordini , giorno con meno ordini , media ordini nel periodo di tempo
#   Quante bevande / pietanze si sono presi in quei giorni'
#   OrdiniAsporto = {'giornoMaxComande':'n_comande' , 'giornoMinComande':'n_comande' , 'MedieComandePeriodoTempo':'n_medioCom', 'Giorno con il maggior numero di elementi':'num_elementi' , 'Giorno con il minor numero di elementi':'num_elementi' , 'mediae elementi':'numMediaElementi'}
#   OrdiniComande = ////
    def generaStatistiche(self):
        OrdiniAsporto , OrdiniTavolo = self.calcolaStatistiche()

        giornoMaxComandeAsporto = max(OrdiniAsporto,key=OrdiniAsporto.get())
        giornoMinComandeAsporto = min(OrdiniAsporto,key=OrdiniAsporto.get())

        giornoMaxComandeTavolo = max(OrdiniTavolo,key=OrdiniTavolo.get())
        giornoMinComandeTavolo = min(OrdiniTavolo,key=OrdiniTavolo.get())

#   OrdineAsporto e OrdineComande hanno la stessa lunghezza(stesso numero di keys), ciò che cambia sono i values al loro interno !

        totAsporto = 0
        elementiOrdineAsporto = {}
        for listaComande in OrdiniAsporto.values():
            totAsporto = totAsporto + len(listaComande)
            numElementi = 0
            for comanda in listaComande:
                  for elemento in comanda.elementiComanda:
                      numElementi = numElementi + 1
            elementiOrdineAsporto[OrdiniAsporto.keys()[OrdiniAsporto.values().index(listaComande)]] = numElementi

        mediaComandeAsporto = round(totAsporto/len(OrdiniAsporto),2)

        giornoNumOrdiniAsportoMax = max(elementiOrdineAsporto,key=elementiOrdineAsporto.get())
        giornoNumOrdiniAsportoMin = min(elementiOrdineAsporto,key=elementiOrdineAsporto.get())
        mediaOrdiniComandeAsporto = round(sum(elementiOrdineAsporto.values())/len(elementiOrdineAsporto),1)

        AsportoPuliti = {}
        AsportoPuliti['MAX : ',giornoMaxComandeAsporto]=OrdiniAsporto.get(giornoMaxComandeAsporto)
        AsportoPuliti['MIN : ',giornoMinComandeAsporto]=OrdiniAsporto.get(giornoMinComandeAsporto)
        AsportoPuliti['Media comande nel periodo di tempo : ']=mediaComandeAsporto
        AsportoPuliti['MAX NUM ELEMENTI COMANDE : ',giornoNumOrdiniAsportoMax]=elementiOrdineAsporto.get(giornoNumOrdiniAsportoMax)
        AsportoPuliti['MIN NUM ELEMENTI COMANDE : ',giornoNumOrdiniAsportoMin]=elementiOrdineAsporto.get(giornoNumOrdiniAsportoMin)
        AsportoPuliti['MEDIA NUM ELEMENTI COMANDE : ']=mediaOrdiniComandeAsporto



        ######### TAVOLO ##########


        giornoMaxComandeAsporto = max(OrdiniAsporto,key=OrdiniAsporto.get())
        giornoMinComandeAsporto = min(OrdiniAsporto,key=OrdiniAsporto.get())

        giornoMaxComandeTavolo = max(OrdiniTavolo,key=OrdiniTavolo.get())
        giornoMinComandeTavolo = min(OrdiniTavolo,key=OrdiniTavolo.get())

#   OrdineAsporto e OrdineComande hanno la stessa lunghezza(stesso numero di keys), ciò che cambia sono i values al loro interno !

        totTavolo = 0
        elementiOrdineTavolo = {}
        for listaComande in OrdiniTavolo.values():
            totTavolo = totTavolo + len(listaComande)
            numElementi = 0
            for comanda in listaComande:
                  for elemento in comanda.elementiComanda:
                      numElementi = numElementi + 1
            elementiOrdineTavolo[OrdiniTavolo.keys()[OrdiniTavolo.values().index(listaComande)]] = numElementi

        mediaComandeTavolo = round(totAsporto/len(OrdiniTavolo),2)

        giornoNumOrdiniTavoloMax = max(elementiOrdineTavolo,key=elementiOrdineTavolo.get())
        giornoNumOrdiniTavoloMin = min(elementiOrdineTavolo,key=elementiOrdineTavolo.get())
        mediaOrdiniComandeTavolo = round(sum(elementiOrdineTavolo.values())/len(elementiOrdineTavolo),1)

        TavoloPuliti = {}
        TavoloPuliti['MAX : ',giornoMaxComandeTavolo]=OrdiniTavolo.get(giornoMaxComandeTavolo)
        TavoloPuliti['MIN : ',giornoMinComandeTavolo]=OrdiniTavolo.get(giornoMinComandeTavolo)
        TavoloPuliti['Media comande nel periodo di tempo : ']=mediaComandeTavolo
        TavoloPuliti['MAX NUM ELEMENTI COMANDE : ',giornoNumOrdiniTavoloMax]=elementiOrdineTavolo.get(giornoNumOrdiniTavoloMax)
        TavoloPuliti['MIN NUM ELEMENTI COMANDE : ',giornoNumOrdiniTavoloMin]=elementiOrdineTavolo.get(giornoNumOrdiniTavoloMin)
        TavoloPuliti['MEDIA NUM ELEMENTI COMANDE : ']=mediaOrdiniComandeTavolo


        return AsportoPuliti , TavoloPuliti
















        
        


