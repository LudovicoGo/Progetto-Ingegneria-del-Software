from RistoMatic.GestioneAttivita.ElementoComanda import ElementoComanda
from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.GestioneAttivita.Enum import StatoComanda
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
import datetime

class Comanda:

    counter_n_comanda=1

    def __init__(self, rif):
        self.dataCreazione = datetime.datetime.now()
        self.elementiComanda= []
        self.rif=rif
        self.sincronizzata=False
        self.numeroComanda = Comanda.counter_n_comanda
        Comanda.counter_n_comanda = Comanda.counter_n_comanda +1

        if isinstance(self.rif, Tavolo):
            self.rif.setIsLibero(False)

        StatoSala.aggiungiComanda(self)

    def aggiornaElementoComanda(self, daAggiornare):
        pass

    def aggiungiElementoComanda(self, elementoDaAggiungere : ElementoComanda):
        self.elementiComanda.append(elementoDaAggiungere)

    def getComandaSincronizzata(self):
        return self.sincronizzata

    def getInfoComanda(self) -> dict:
        rif=""
        if isinstance(self.rif, Tavolo):
            rif = "Tavolo "+ str(self.rif.getRiferimentoTavolo())
        elif isinstance(self.rif,OrdineAsporto):
            rif = "Asporto " + str(self.rif.getNumeroOrdine())
        return {
            "rif": rif,
            "dataCreazione": self.dataCreazione,
            "numeroComanda": self.numeroComanda,
            "sincronizzata": self.sincronizzata
        }

    def getNumeroComanda(self) -> int:
        return self.numeroComanda

    def getStato(self):
        count=0
        for elemento in self.elementiComanda:
            if elemento.getIsPronta():
                count=count+1

        if count==len(self.elementiComanda):
            return StatoComanda.COMPLETATA
        elif count > 0:
            return StatoComanda.AVVIATA
        else:
            return StatoComanda.NON_AVVIATA

    def inviaNotificaBar(self):
        pass

    def rimuoviElementoComanda(self, daEliminare : ElementoComanda):
        self.elementiComanda.remove(daEliminare)

    def setComandaSincronizzata(self, comandaSincronizzata : bool):
        self.sincronizzata=comandaSincronizzata

    def setStatoPreparazione(self, stato : StatoComanda):
        for elemento in self.elementiComanda:
            if stato==StatoComanda.COMPLETATA:
                elemento.setIsPronta(True)
            elif stato==StatoComanda.NON_AVVIATA:
                elemento.setIsPronta(False)

    def stampaPreconto(self):
        pass

    def getCostoCoperto(self):
        if isinstance(self.rif, Tavolo):
            tot=self.rif.getNumeroCoperti()*StatoSala.getMenuAttivo().getCostoCoperto()
            return tot
        return 0

    def getTotale(self):
        tot=0
        for elemento in self.elementiComanda:
            qnt = elemento.getQuantita()
            info = elemento.getInfoElementoComanda()
            tot = tot+ (qnt*info["Prezzo"])

        tot = tot+ self.getCostoCoperto()
        return tot

    @staticmethod
    def ricercaComanda(riferimentoTavolo : int):
        for comanda in StatoSala.getComande():
            if isinstance(comanda.rif,Tavolo) and comanda.rif.riferimentoTavolo==riferimentoTavolo:
                return comanda
        return None

    def rimuoviComanda(self):
        if isinstance(self.rif, Tavolo):
            self.rif.setIsLibero(True)
            self.rif.setNumeroCoperti(0)
        StatoSala.rimuoviComanda(self)
        del self
