from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.GestioneAttivita.Enum import Zone


class ElementoComanda():
    def __init__(self, elementoMenu : ElementoMenu, note: str, quantita: int):
        self.elemento = elementoMenu
        self.note = note
        self.quantita=quantita
        self.isPronta = False
        #self.visibilita = False

    def getInfoElementoComanda(self) -> dict:
        return {"Nome":self.elemento.nomeElemento,
                "Note":self.note,
                "Quantita":self.quantita}

    def getIsPronta(self) -> bool:
        return self.stato

    def getNote(self) -> str:
        return self.note

    def getQuantita(self) -> int:
        return self.quantita

    #def getVisibilita(self) -> Zone:
    #    return self.visibilita

    def setIsPronta(self,isPronta : bool):
        self.stato=isPronta

    def setNote(self,note : str) :
        self.note=note

    def setQuantita(self,quantita : int):
        self.quantita=quantita

    #def setVisibilita(self,visibilita : Zone) :
    #    self.visibilita=visibilita