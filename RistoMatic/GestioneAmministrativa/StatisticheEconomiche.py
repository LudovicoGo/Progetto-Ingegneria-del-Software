
# Statistiche su MASSIMO INCASSO , MINIMO INCASSO , TOTALE INCASSO NEL FILTRO CORRENTE
# Se non presente nessun fitro verra utilizzato uno di default

import datetime
import pickle

from GestioneAmministrativa.Statistiche import Statistiche
from GestioneAttivita import StatoSala

class StatisticheEconomiche(Statistiche):




    def __init__(self, dataInizio , dataFine):
        super.__init__(dataInizio , dataFine)


    # Dati "rozzi" , da lavorare
    def calcolaStatistiche(self) -> dict:
        if ( self.dataInizio is None) or (self.dataFine is None) :
            self.dataFine = datetime.date.today()
            self.dataInizio = datetime.datetime.today() - datetime.timedelta(days=1)


        storicoComande = []
        with (open("Comande.pickle", "rb")) as openfile:
           while True:
             try:
                storicoComande = pickle.load(openfile)
             except EOFError:
                 break

        # Creo la lista delle date:

        # L'idea è registrare gli incassi giorno per giorno , faccio un dizionario con giorno e incasso
        incasso = {}

        data = self.dataInizio
        for comanda in storicoComande:
            tot = 0
            while data <= self.dataFine:
                if comanda.dataCreazione == data :
                    tot += comanda.getTotale()
                data += datetime.timedelta(days = 1)
            incasso.pop(data,tot)

        return incasso





    def generaStatistiche(self)->dict:

        datiGrezzi = self.calcolaStatistiche()

        giornoMaxIncasso  = max(datiGrezzi, key=datiGrezzi.get)
        giornoMinIncasso = min(datiGrezzi , key=datiGrezzi.get)

        mediaIncasso = 0
        for singoloIncasso in datiGrezzi.__len__():
            mediaIncasso += singoloIncasso

        datiRaffinati = {}
        datiRaffinati.pop(giornoMaxIncasso,datiGrezzi.get(giornoMaxIncasso))
        datiRaffinati.pop(giornoMinIncasso,datiGrezzi.get(giornoMinIncasso))
        datiRaffinati.pop("media incassi: ",datiGrezzi.get(mediaIncasso))

        return datiRaffinati




































