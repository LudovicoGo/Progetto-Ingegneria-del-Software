from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione


class ClasseTestLudovico():
    def __init__(self):
        self.cliente = Cliente('Albertino', '987654321')
        self.cliente2 = Cliente('Michelino', '123456789')
        self.cliente3 = Cliente('Faustino', '123789456')

      #  @staticmethod
        self.PRENOTAZIONI = [Prenotazione('dd/mm/yyyy1', 5, 'Confermata', self.cliente, 4),
                             Prenotazione('dd/mm/yyyy2', 1, 'Da Confermare', self.cliente3, 10),
                             Prenotazione('dd/mm/yyyy3', 3, 'Da Confermare', self.cliente2, 6),
                             Prenotazione('dd/mm/yyyy4', 17, 'Confermata', self.cliente, 2),
                             Prenotazione('dd/mm/yyyy5', 14, 'Confermata', self.cliente3, 44),
                             Prenotazione('dd/mm/yyyy6', 6, 'Confermata', self.cliente2, 47),
                             Prenotazione('dd/mm/yyyy7', 8, 'Confermata', self.cliente2, 887),
                             Prenotazione(dataPrenotazione='dd/mm/yyyy', numeroPersone=21,
                                          statoPrenotazione='Confermata',
                                          cliente=self.cliente2, riferimentoTavolo=7)]


        self.ASPORTO = [OrdineAsporto('21:00', '19:30', self.cliente), OrdineAsporto('21:00', '19:30', self.cliente), OrdineAsporto('19:00', '16:30', self.cliente2), OrdineAsporto('20:00', '15:30', self.cliente2), OrdineAsporto('22:00', '19:30', self.cliente3)]

    def ricercaNomeDataTavolo(self, nomeCliente, dataPrenotazione, riferimentoTavolo):
        for i in self.PRENOTAZIONI:
            if i.cliente.nomeCliente == nomeCliente and i.riferimentoTavolo == int(riferimentoTavolo):
                prenotazione = i
        return self.PRENOTAZIONI.index(prenotazione)


    def ricercaNomeRecapitoTavolo(self, nomeCliente, recapitoTelefonico, riferimentoTavolo):
       for i in self.PRENOTAZIONI:
            if i.cliente.nomeCliente == nomeCliente and i.riferimentoTavolo == int(riferimentoTavolo):
                prenotazione = i
       return prenotazione


    def stampaLista(self):
        count = 1
        for i in self.PRENOTAZIONI:
            print(count, i.getInfoPrenotazione())
            count += 1