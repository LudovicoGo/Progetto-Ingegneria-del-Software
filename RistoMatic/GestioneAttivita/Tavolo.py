from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Enum import StatoTavolo
import datetime

class Tavolo():
    counter_n_tavolo = 1

    def __init__(self, posti):
        super(Tavolo, self).__init__()
        self.riferimentoTavolo=Tavolo.counter_n_tavolo
        self.numeroPosti=posti
        self.numeroCoperti=0
        self.isLibero = True
        StatoSala.aggiungiTavolo(self)
        Tavolo.counter_n_tavolo = Tavolo.counter_n_tavolo + 1

    def getInfoTavolo(self) -> dict:
        return {
            "riferimentoTavolo": self.riferimentoTavolo,
            "coperti": self.coperti,
            "libero": self.isLibero
        }

    def getIsLibero(self) -> bool:
        return (not self.isLibero and not self.getIsPrenotato())

    def getIsPrenotato(self) -> bool:
        prenotazioni=StatoSala.getListaPrenotazioni()
        if (not prenotazioni == None):
            now = datetime.datetime.now()
            for prenotazione in prenotazioni:
                tavoloprenotato=prenotazione.getTavoloPrenotato()
                dataprenotazione= prenotazione.dataPrenotazione
                diff = (now - dataprenotazione)
                if tavoloprenotato == self.riferimentoTavolo and (diff.total_seconds()/3600 < 4):
                    return True
        return False

    def getNumeroCoperti(self) -> int:
        return self.numeroCoperti

    def getNumeroPosti(self) -> int:
        return self.numeroPosti

    def getRiferimentoTavolo(self) -> int:
        return self.riferimentoTavolo

    def setIsLibero(self, tavoloLibero : bool):
        self.isLibero=tavoloLibero

    def setNumeroCoperti(self, numeroCoperti: int):
        self.numeroCoperti = numeroCoperti

    def setNumeroPosti(self, numeroPosti : int):
        self.numeroPosti=numeroPosti

    def getStato(self):
        if(not self.isLibero):
            return StatoTavolo.OCCUPATO
        elif(self.getIsPrenotato()):
            return StatoTavolo.PRENOTATO
        return StatoTavolo.UTILIZZABILE
