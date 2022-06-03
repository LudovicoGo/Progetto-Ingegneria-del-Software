import ElementoComanda
import Tavolo
import OrdineAsporto
from Enum import StatoComanda
import datetime

class Comanda:

    counter_n_comanda=1

    def __init__(self, rif):
        self.dataCreazione = datetime.datetime.now()
        self.ElementiComanda= []
        self.rif=rif
        self.sincronizzata=False
        self.numeroComanda = Comanda.counter_n_comanda
        Comanda.counter_n_comanda = Comanda.counter_n_comanda +1

    def aggiornaElementoComanda(self, daAggiornare):
        pass

    def aggiungiElementoComanda(self, elementoDaAggiungere : ElementoComanda):
        self.ElementiComanda.append(elementoDaAggiungere)

    def getComandaSincronizzata(self):
        return self.sincronizzata

    def getInfoComanda(self) -> dict:
        pass

    def getNumeroComanda(self) -> int:
        return self.numeroComanda

    def getStatoPrenotazione(self):
        count=0
        for elemento in self.ElementiComanda:
            if elemento.getIsPronto():
                count=count+1

        if count==self.ElementiComanda.count():
            return StatoComanda.COMPLETATA
        elif count > 0:
            return StatoComanda.AVVIATA
        else:
            return StatoComanda.NON_AVVIATA

    def inviaNotificaBar(self):
        pass

    def rimuoviElementoComanda(self, daEliminare : ElementoComanda):
        self.ElementiComanda.remove(daEliminare)

    def setComandaSincronizzata(self, comandaSincronizzata : bool):
        self.sincronizzata=comandaSincronizzata

    def setStatoPreparazione(self, stato : StatoComanda):
        for elemento in self.ElementiComanda:
            if stato==StatoComanda.COMPLETATA:
                elemento.setIsPronta(True)
            elif stato==StatoComanda.NON_AVVIATA:
                elemento.setIsPronta(False)

    def stampaPreconto(self):
        pass