from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione


class ClasseTestLudovico():
    def __init__(self):

        self.cliente = Cliente('Albertino', '987654321')
        self.cliente2 = Cliente('Michelino', '123456789')
        self.cliente3 = Cliente('Faustino', '123789456')

        self.PRENOTAZIONI = [Prenotazione('dd/mm/yyyy', 5, 'Confermata', self.cliente, 4),
                             Prenotazione('dd/mm/yyyy', 1, 'Da Confermare', self.cliente3, 10),
                             Prenotazione('dd/mm/yyyy', 3, 'Da Confermare', self.cliente2, 6),
                             Prenotazione('dd/mm/yyyy', 17, 'Confermata', self.cliente, 2),
                             Prenotazione('dd/mm/yyyy', 14, 'Confermata', self.cliente3, 44),
                             Prenotazione('dd/mm/yyyy', 6, 'Confermata', self.cliente2, 47),
                             Prenotazione('dd/mm/yyyy', 8, 'Confermata', self.cliente2, 887),
                             Prenotazione(dataPrenotazione='dd/mm/yyyy', numeroPersone=21, statoPrenotazione='Confermata',
                                          cliente=self.cliente2, riferimentoTavolo=7)]



    def ricercaNomeDataTavolo(self, nomeCliente, dataPrenotazione, riferimentoTavolo):
        for i in range(0, len(self.PRENOTAZIONI)):
            if self.PRENOTAZIONI[i].cliente.nomeCliente == nomeCliente and self.PRENOTAZIONI[i].dataPrenotazione == dataPrenotazione and self.PRENOTAZIONI[i].riferimentoTavolo == riferimentoTavolo:
                return i
            i = i+1
        return -1

    def ricercaNomeRecapitoTavolo(self, nomeCliente, recapitoTelefonico, riferimentoTavolo):
       for i in self.PRENOTAZIONI:
            if i.cliente.nomeCliente == nomeCliente and i.riferimentoTavolo == int(riferimentoTavolo):
                prenotazione = i
       return prenotazione


    def stampaLista(self):
        for i in self.PRENOTAZIONI:
            print(i.getInfoPrenotazione())
