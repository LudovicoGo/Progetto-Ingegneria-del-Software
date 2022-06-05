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
        #self.isPrenotato = False
        self.nomeTavolo=""
        StatoSala.Tavoli.append(self)

    def getInfoTavolo(self) -> dict:
        return {
            "riferimentoTavolo": self.riferimentoTavolo,
            "coperti": self.coperti,
            "libero": self.isLibero
        }

    def getIsLibero(self) -> bool:
        return self.isLibero

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

    #def setIsPrenotato(self,tavoloPrenotato : bool):
        #pass

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