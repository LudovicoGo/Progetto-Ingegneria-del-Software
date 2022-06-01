class ElementoMenu():

    def __init__(self, area, nome, prezzo):
        self.areaPreparazione = area
        self.nomeElemento = nome
        self.prezzoElemento = prezzo

    def __eq__(self, name):
        return self.nomeElemento == name

    def getAreaPreparazione(self):
        return self.areaPreparazione

    def getNomeElemento(self):
        return self.nomeElemento

    def getPrezzoElemento(self):
        return self.prezzoElemento

    def setAreaPreparazione(self, area):
        self.areaPreparazione = area

    def setPrezzoElemento(self, prezzo):
        self.prezzoElemento = prezzo

    def setNomeElemento(self, nome):
        self.nomeElemento = nome
