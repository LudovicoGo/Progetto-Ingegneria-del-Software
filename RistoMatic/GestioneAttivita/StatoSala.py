import datetime

import RistoMatic.GestioneAttivita.Tavolo


class StatoSala():
    OrdiniAsporto =[]
    Tavoli = []
    Prenotazioni = []
    Comande = []
    ListaMenu = []
    Menu = ""

    def __init__(self):
        pass

    @staticmethod
    def aggiungiTavolo(tavolo):
        StatoSala.Tavoli.append(tavolo)

    @staticmethod
    def aggiungiComanda(comanda):
        StatoSala.Comande.append(comanda)
        if isinstance(comanda.rif, RistoMatic.GestioneAttivita.Tavolo.Tavolo):
            comanda.rif.setIsLibero(False)

    @staticmethod
    def aggiungiMenu(menu):
        StatoSala.ListaMenu.append(menu)

    @staticmethod
    def getTavoli():
        return StatoSala.Tavoli

    @staticmethod
    def getComande():
        return StatoSala.Comande

    @staticmethod
    def getMenuAttivo():
        return StatoSala.Menu

    @staticmethod
    def setMenuAttivo(menu):
        StatoSala.Menu=menu

    @staticmethod
    def getListaMenu():
        return StatoSala.ListaMenu

    @staticmethod
    def rimuoviTavolo(tavolo):
        StatoSala.Tavoli.remove(tavolo)

    @staticmethod
    def rimuoviComanda(comanda):
        StatoSala.Comande.remove(comanda)
        if isinstance(comanda.rif, RistoMatic.GestioneAttivita.Tavolo.Tavolo):
            comanda.rif.setIsLibero(True)
            comanda.rif.setNumeroCoperti(0)

    @staticmethod
    def rimuoviMenu(menu):
        StatoSala.ListaMenu.remove(menu)

    def aggiungiOrdineAsporto(self,oraConsegna : datetime):
        pass

    def confermaPrenotazione(self, daConfermare):
        pass

    def createPrenotazione(self, daCreare):
        pass

    def getListaAsporto(self) -> dict:
        pass

    def getListaCodaPrenotazione(self) -> dict:
        pass

    def getListaPrenotazioni(self) -> dict:
        pass

    def getPrenotazione(self,nomeCliente : str, data : datetime):
        pass

    def inviaRisposta(self) :
        pass

    def modificaOrdineAsporto(self,nomeCliente : str):
        pass

    def notificaDisponibilita(self,numeroCellulareCliente : str, nomeCliente : str):
        pass

    def ricercaPrenotazione(self, nomeCliente : str, dataPrenotazione : datetime):
        pass

    def rimuoviOrdineAsporto(self,nomeCliente : str):
        pass

    def rimuoviPrenotazioniNonConfermate(self):
        pass

