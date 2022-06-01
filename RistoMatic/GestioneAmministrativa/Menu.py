import datetime
import ElementoMenu

class Menu:
    def __init__(self,):
        self.costoCoperto=0
        self.dataCreazione = datetime.datetime.now()
        self.nomeMenu=""
        self.listaElementi = []

    def aggiungiElementoMenu(self, elemento):
        self.listaElementi.append(elemento)

    def eliminaElementoMenu(self, nome):
        self.listaElementi.remove(nome)

    def getCostoCoperto(self):
        return self.costoCoperto

    def getDataCreazione(self):
        return self.dataCreazione

    def getNomeMenu(self):
        return self.nomeMenu

    def setCostoCoperto(self, costo):
        self.costoCoperto=costo

    def setDataCreazione(self, data):
        self.dataCreazione = datetime.datetime.strptime(data)

    def setNomeMenu(self, nome):
        if isinstance(nome, str):
            self.nomeMenu = nome