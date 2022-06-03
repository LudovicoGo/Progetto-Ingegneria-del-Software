import datetime
import ElementoMenu

class Menu:
    def __init__(self, costo_coperto=0, nome_menu=""):
        self.costoCoperto=costo_coperto
        self.dataCreazione = datetime.datetime.now()
        self.nomeMenu=nome_menu
        self.listaElementi = dict()

    def aggiungiElementoMenu(self, elemento: ElementoMenu):
        self.listaElementi[elemento.nomeElemento] = elemento

    def aggiornaElementoMenu(self, elemento_nuovo: ElementoMenu):
        self.listaElementi[elemento_nuovo.nomeElemento] = elemento_nuovo

    def eliminaElementoMenu(self, nome: str):
        del(self.listaElementi[nome])

    def eliminaElementoMenu(self, elemento: ElementoMenu):
        del(self.listaElementi[elemento.nomeElemento])

    def getCostoCoperto(self):
        return self.costoCoperto

    def getDataCreazione(self):
        return self.dataCreazione

    def getInfoMenu(self):
        return {
            "nomeMenu": self.nomeMenu,
            "costoCoperto": self.costoCoperto,
            "dataCreazione": self.dataCreazione
        }

    def getNomeMenu(self):
        return self.nomeMenu

    def getListaElementi(self):
        return self.listaElementi

    def setCostoCoperto(self, costo):
        self.costoCoperto=costo

    def setDataCreazione(self, data):
        self.dataCreazione = datetime.datetime.strptime(data, "%d/%m/%Y")

    def setNomeMenu(self, nome: str):
        if isinstance(nome, str):
            self.nomeMenu = nome