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

        storicoComande = []
    with (open("Comande.pickle", "rb")) as openfile:
        while True:
             try:
                storicoComande = pickle.load(openfile)
             except EOFError:
                 break

    OrdiniAsporto = {}
    OrdiniTavolo = {}
    for comanda in storicoComande:



