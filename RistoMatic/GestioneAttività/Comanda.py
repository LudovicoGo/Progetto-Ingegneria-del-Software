import ElementoComanda
import Tavolo

class Comanda:

    numerocomanda=1

    def __init__(self, tavolo : Tavolo):
        self.ElementoComanda= []
        self.tavolo=tavolo
        Comanda.numerocomanda = Comanda.numerocomanda +1

    def __init__(self, ordineasp: OrdineAsporto):
        self.ElementoComanda = []
        self.OrdineAsporto = ordineasp

    def aggiornaElementoComanda(self, daAggiornare):
        pass

    def aggiungiElementoComanda(self, elementoDaAggiungere : ElementoComanda):
        self.ElementoComanda.append(elementoDaAggiungere)

    def getComandaSincronizzata(self):
        pass

    def getInfoComanda(self) -> dict:
        pass

    def getNumeroComanda(self) -> int:
        pass

    def getStatoPrenotazione(self) -> bool:
        pass

    def inviaNotificaBar(self):
        pass

    def rimuoviElementoComanda(self, daEliminare : ElementoComanda):
        self.ElementoComanda.remove(daEliminare)

    def setComandaSincronizzata(self, comandaSincronizzata : bool):
        pass

    def setStatoPreparazione(self, stato : bool):
        pass

    def stampaPreconto(self):
        pass