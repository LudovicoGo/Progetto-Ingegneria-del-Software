import ElementoMenu
from EnumZone import Zone


class ElementoComanda():
    def __init__(self, elementoMenu : ElementoMenu, note, quantita):
        self.elemento = elementoMenu
        self.note = note
        self.quantita=quantita
        self.stato = False
        #self.visibilita =

    def __init__(self):
        pass

    def getInfoElementoComanda(self) -> dict:
        return {"Nome":self.elemento,
                "Note":self.note,
                "qty":self.quantita}

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