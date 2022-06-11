import datetime
import os
import pickle

import RistoMatic.GestioneAttivita.Tavolo
import RistoMatic.GestioneAttivita.OrdineAsporto
from RistoMatic.GestioneAttivita.Enum import StatoComanda


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
    def getTavoli():
        return StatoSala.Tavoli

    @staticmethod
    def aggiungiTavolo(tavolo):
        StatoSala.Tavoli.append(tavolo)

    @staticmethod
    def ricercaTavolo(tavolo_ricerca):
        rif=0
        if isinstance(tavolo_ricerca, RistoMatic.GestioneAttivita.Tavolo.Tavolo):
            rif= tavolo_ricerca.riferimentoTavolo
        elif isinstance(tavolo_ricerca, int):
            rif = tavolo_ricerca

        for tavolo in StatoSala.getTavoli():
            if tavolo.riferimentoTavolo == rif:
                return tavolo
        return None

    @staticmethod
    def rimuoviTavolo(tavolo):
        StatoSala.Tavoli.remove(tavolo)


    @staticmethod
    def getComande():
        return StatoSala.Comande

    @staticmethod
    def aggiungiComanda(comanda):
        StatoSala.Comande.append(comanda)
        if isinstance(comanda.rif, RistoMatic.GestioneAttivita.Tavolo.Tavolo):
            comanda.rif.setIsLibero(False)

    @staticmethod
    def ricercaComanda(riferimento: int):
        for comanda in StatoSala.getComande():
            if isinstance(comanda.rif, RistoMatic.GestioneAttivita.Tavolo.Tavolo) and comanda.rif.riferimentoTavolo == riferimento:
                return comanda
            elif isinstance(comanda.rif, RistoMatic.GestioneAttivita.OrdineAsporto.OrdineAsporto) and comanda.rif.numeroOrdine == riferimento:
                return comanda
        return None

    @staticmethod
    def rimuoviComanda(comanda):
        if (comanda.getStato()==StatoComanda.COMPLETATA or comanda.getStato() == StatoComanda.ANNULLATA ):
            dati = []
            if os.path.isfile('Dati/Comande.pickle'):
                with open('Dati/Comande.pickle', 'rb') as f:
                    dati = pickle.load(f)
            dati.append(comanda)
            with open('Dati/Comande.pickle', 'wb') as handle:
                pickle.dump(dati, handle, pickle.HIGHEST_PROTOCOL)

            StatoSala.Comande.remove(comanda)
            if isinstance(comanda.rif, RistoMatic.GestioneAttivita.Tavolo.Tavolo):
                comanda.rif.setIsLibero(True)
                comanda.rif.setNumeroCoperti(0)


    @staticmethod
    def getListaMenu():
        return StatoSala.ListaMenu

    @staticmethod
    def aggiungiMenu(menu):
        StatoSala.ListaMenu.append(menu)

    @staticmethod
    def getMenuAttivo():
        return StatoSala.Menu

    @staticmethod
    def setMenuAttivo(menu):
        StatoSala.Menu=menu

    @staticmethod
    def rimuoviMenu(menu):
        StatoSala.ListaMenu.remove(menu)



    def aggiungiOrdineAsporto(self,oraConsegna : datetime):
        pass

    def confermaPrenotazione(self, daConfermare):
        pass

    def createPrenotazione(self, daCreare):
        pass

    def getListaAsporto(self):
        return StatoSala.OrdiniAsporto

    def getListaCodaPrenotazione(self) -> dict:
        pass

    @staticmethod
    def getListaPrenotazioni() -> dict:
        pass

    def getPrenotazione(self,nomeCliente : str, data : datetime):
        pass

    def inviaRisposta(self):
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

