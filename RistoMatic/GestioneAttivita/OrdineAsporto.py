class OrdineAsporto():
    id = 0

    def __init__(self, oraConsegna, oraOrdine):
        self.numeroOrdine = self.id
        self.id += 1
        self.oraConsegna = oraConsegna
        self.oraOrdine = oraOrdine

    def getInfoOrdineAsporto(self):
        return {
            "numeroOrdine": self.numeroOrdine,
            "oraOrdine": self.oraOrdine,
            "oraConsegna": self.oraConsegna
        }

    def getNumeroOrdine(self):
        return self.numeroOrdine

    def getOraConsegna(self):
        return self.oraConsegna

    def getoraOrdine(self):
        return self.oraOrdine

    def setOraConsegna(self, oraConsegna):
        self.oraConsegna = oraConsegna

    def setoraOrdine(self, oraOrdine):
        self.oraOrdine = oraOrdine
        