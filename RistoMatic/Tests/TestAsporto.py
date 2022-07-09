import unittest
from datetime import datetime

from PyQt5.QtWidgets import QMessageBox

from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.Viste.VistaAggiungiOrdineAsporto import VistaAggiungiOrdineAsporto


class TestAsporto(unittest.TestCase):

   def classeAsporto(self):
#      Dati Cliente , Asporto :
       cliente = Cliente('Mario Rossi','3701159871')
       data = datetime.datetime(2022, 6, 14, 19, 30, 0)
       data.now()
       from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
       ordineAsporto = OrdineAsporto(data.now,data,cliente)
#      ************************
       self.assertEqual(cliente.nomeCliente,ordineAsporto.cliente.nomeCliente)
       self.assertEqual(ordineAsporto.getoraOrdine(),data)
       self.assertEqual(ordineAsporto.getOraConsegna(),data.now())


