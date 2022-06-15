from RistoMatic.GestioneAttivita.Cliente import Cliente


class Prenotazione():

    id = 0

    def __init__(self, dataPrenotazione, numeroPersone, statoPrenotazione, cliente: Cliente, riferimentoTavolo):
        self.idPrenotazione = self.id
        self.id += 1
        self.dataPrenotazione = dataPrenotazione
        self.numeroPersone = numeroPersone
        self.statoPrenotazione = "Confermata"

        self.cliente = cliente
        self.riferimentoTavolo = riferimentoTavolo


    def getTavoloPrenotato(self):
        return self.riferimentoTavolo

    def getInfoPrenotazione(self):
        return {
            "nomeCliente": self.cliente.getNomeCliente(),
            "idCliente": self.cliente.getIdCliente(),
            "recapitoTelefonico": self.cliente.getRecapitoTelefonico(),
            "idPrenotazione": self.idPrenotazione,
            "dataPrenotazione": self.dataPrenotazione,
            "numeroPersone": self.numeroPersone,
            "statoPrenotazione": self.statoPrenotazione,
            "riferimentoTavolo": self.riferimentoTavolo
        }

    def getDataPrenotazione(self):
        return self.dataPrenotazione

    def getIdPrenotazione(self):
        return self.idPrenotazione

    def getNumeroPersone(self):
        return self.numeroPersone

    def getStatoPrenotazione(self):
        return self.statoPrenotazione

    def setDataPrenotazione(self, dataPrenotazione):
        self.dataPrenotazione = dataPrenotazione

    def setNumeroPersone(self, NumeroPersone):
        self.numeroPersone = NumeroPersone

    def setStatoPrenotazione(self, statoPrenotazione):
        self.statoPrenotazione = statoPrenotazione

    def getRiferimentoTavolo(self):
        return self.riferimentoTavolo

    def setRiferimentoTavolo(self, riferimentoTavolo):
        self.riferimentoTavolo = riferimentoTavolo

