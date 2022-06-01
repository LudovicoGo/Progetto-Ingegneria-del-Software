from PySide6 import QtCore
from PySide6.QtCore import Signal,Slot
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class Tavolo(QtCore.QObject):
    numero = 1
    update_ui = Signal()


    def __init__(self, coperti, stat):
        super(Tavolo, self).__init__()
        self.numero=Tavolo.numero
        Tavolo.numero =Tavolo.numero+1
        self.coperti=coperti
        self.stat =stat

    def aggiungitavolo(self,):
        StatoSala.Tavoli.append(self)
        self.update_ui.emit()

    def getInfoTavolo(self) -> dict:
        pass

    def getIsLibero(self) -> bool:
        pass

    def getIsPrenotato(self) -> bool:
        pass

    def getNomeTavolo(self) -> str:
        pass

    def getNumeroCoperti(self) -> int:
        pass

    def getRiferimentoTavolo(self) -> int:
        pass

    def setIsLibero(self, tavoloLibero : bool):
        pass

    def setIsPrenotato(self,tavoloPrenotato : bool):
        pass

    def setNomeTavolo(self,nomeTavolo : str):
        pass

    def setNumeroCoperti(self, numeroCoperti : int):
        pass