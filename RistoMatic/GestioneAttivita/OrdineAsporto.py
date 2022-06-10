import RistoMatic.GestioneAttivita.Comanda

class OrdineAsporto():
    id = 0

    def __init__(self, oraConsegna, oraOrdine, cliente):
        self.numeroOrdine = self.id
        self.id += 1
        self.oraConsegna = oraConsegna
        self.oraOrdine = oraOrdine
        self.cliente = cliente

        self.comanda = RistoMatic.GestioneAttivita.Comanda(id)

    def getInfoOrdineAsporto(self):
        return {
            "numeroOrdine": self.numeroOrdine,
            "oraOrdine": self.oraOrdine,
            "oraConsegna": self.oraConsegna,

            "nomeCliente": self.cliente.getNomeCliente(),
            "recapitoTelefonico": self.cliente.getRecapitoTelefonico(),
            "idCliente": self.cliente.getIdCliente()
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

    def aggiungiElementoAporto(self, elementoComanda):
        self.comanda.elementiComanda.append(elementoComanda)

    def rimuoviElementoAporto(self, index):
        self.comanda.elementiComanda.remove(index)

