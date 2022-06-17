import unittest

from RistoMatic.GestioneAttivita.Tavolo import Tavolo
from RistoMatic.GestioneAttivita.Comanda import Comanda

class TestComanda(unittest.TestCase):

    def test_creazione_tavolo(self):
        tavolo= Tavolo(1)
        comanda=Comanda(tavolo)
        assert(comanda.getNumeroComanda()==1 and isinstance(comanda.rif,Tavolo))

