
# Statistiche su MASSIMO INCASSO , MINIMO INCASSO , TOTALE INCASSO NEL FILTRO CORRENTE
# Se non presente nessun fitro verra utilizzato uno di default

import datetime
from GestioneAmministrativa.Statistiche import Statistiche
from GestioneAttivita import StatoSala

class StatisticheEconomiche(Statistiche):

    def __init__(self, dataInizio , dataFine):
        super.__init__(dataInizio , dataFine)


    def calcolaStatistiche(self):
        if ( self.dataInizio is None) or (self.dataFine is None) :
            self.dataFine = datetime.date.today()
            self.dataInizio = datetime.datetime.today() - datetime.timedelta(days=1)

    # Acquisisco gli incassi sul asporto:

    for asporto in StatoSala.StatoSala.getListaAsporto():






