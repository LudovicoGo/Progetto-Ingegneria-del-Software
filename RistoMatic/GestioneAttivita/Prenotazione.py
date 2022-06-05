from RistoMatic.GestioneAttivita.Cliente import Cliente


class Prenotazione():

    id = 0

    def __init__(self, dataPrenotazione, numeroPersone, statoPrenotazione, cliente: Cliente, riferimentoTavolo):
        self.idPrenotazione = self.id
        self.id += 1
        self.dataPrenotazione = dataPrenotazione
        self.numeroPersone = numeroPersone
        self.statoPrenotazione = statoPrenotazione

        self.cliente = cliente
        self.riferimentoTavolo = riferimentoTavolo


    def getInfoPrenotazione(self):
        return {
            "idPrenotazione": self.idPrenotazione,
            "dataPrenotazione": self.dataPrenotazione,
            "numeroPersone": self.numeroPersone,
            "statoPrenotazione": self.statoPrenotazione
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
        self.NumeroPersone = NumeroPersone

    def setStatoPrenotazione(self, statoPrenotazione):
        self.StatoPrenotazione = statoPrenotazione

    def getRiferimentoTavolo(self):
        return self.riferimentoTavolo

    def setRiferimentoTavolo(self, riferimentoTavolo):
        self.riferimentoTavolo = riferimentoTavolo

