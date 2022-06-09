from PySide6 import QtCore
from PySide6.QtCore import Signal,Slot
from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Enum import StatoTavolo
import datetime

class Tavolo():
    counter = 1

    def __init__(self, posti):
        super(Tavolo, self).__init__()
        self.riferimentoTavolo=Tavolo.counter
        Tavolo.counter = Tavolo.counter + 1
        self.posti=posti
        self.coperti=0
        self.isLibero = True
        self.nomeTavolo=""
        StatoSala.aggiungiTavolo(self)

    def getInfoTavolo(self) -> dict:
        return {
            "riferimentoTavolo": self.riferimentoTavolo,
            "coperti": self.coperti,
            "libero": self.isLibero
        }

    def getIsLibero(self) -> bool:
        return (not self.isLibero and not self.getIsPrenotato())

    def getIsPrenotato(self) -> bool:
        prenotazioni=StatoSala.Prenotazioni
        now = datetime.datetime.now()
        for prenotazione in prenotazioni:
            tavoloprenotato=prenotazione.getTavoloPrenotato()
            dataprenotazione= prenotazione.dataPrenotazione()
            diff = (now - dataprenotazione)
            if tavoloprenotato.riferimentoTavolo == self.riferimentoTavolo and (diff.total_seconds()/3600 < 4):
                return True

        return False

    def getNomeTavolo(self) -> str:
        return self.nomeTavolo

    def getNumeroCoperti(self) -> int:
        return self.coperti

    def getRiferimentoTavolo(self) -> int:
        return self.riferimentoTavolo

    def setIsLibero(self, tavoloLibero : bool):
        self.isLibero=tavoloLibero

    def setNomeTavolo(self,nomeTavolo : str):
        self.nomeTavolo=nomeTavolo

    def setNumeroCoperti(self, numeroCoperti : int):
        self.coperti=numeroCoperti

    def getStato(self):
        if(self.getIsPrenotato()):
            return StatoTavolo.PRENOTATO
        elif(not self.isLibero):
            return StatoTavolo.OCCUPATO
        return StatoTavolo.UTILIZZABILE

    def rimuoviTavolo(self):
        StatoSala.rimuoviTavolo(self)
        del self

    @staticmethod
    def ricercaTavolo(tavolo_ricerca):
        rif=0
        if isinstance(tavolo_ricerca, Tavolo):
            rif= tavolo_ricerca.riferimentoTavolo
        elif isinstance(tavolo_ricerca, int):
            rif = tavolo_ricerca

        for tavolo in StatoSala.getTavoli():
            if tavolo.riferimentoTavolo == rif:
                return tavolo
        return None
