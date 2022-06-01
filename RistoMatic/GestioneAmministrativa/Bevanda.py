import ElementoMenu

class Bevanda(ElementoMenu):
    def __init__(self,):
        pass

    def getContenitoreBevanda(self):
        return self.contenitoreBevanda

    def getTemperaturaBevanda(self):
        return self.temperaturaBevanda

    def aggiungiContenitoreBevanda(self, contenitore):
        self.contenitoreBevanda.append(contenitore)

    def eliminaContenitoreBevanda(self, contenitore):
        self.contenitoreBevanda.remove(contenitore)

    def setTemperaturaBevanda(self, temp):
        self.temperaturaBevanda = temp
