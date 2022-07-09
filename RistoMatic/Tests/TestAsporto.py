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


   def vistaAggiungiOrdineAsporto(self):
#      Dati Cliente , Asporto :
       cliente = Cliente('Mario Rossi 12345','37011598BHI1')
       data = datetime.datetime(2022, 6, 14, 19, 30, 0)
       data.now()
       from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
       ordineAsporto = OrdineAsporto(data.now,data,cliente)
#      ************************

       vistaAggiungiOrdineAsporto = VistaAggiungiOrdineAsporto()
       vistaAggiungiOrdineAsporto.show()
       msg = QMessageBox()
       msg.hide()
       msg.setWindowTitle('ATTENZIONE!')
       msg.setIcon(QMessageBox.Critical)
       msg.setText("ERRORE!")
       msg.setInformativeText("Compilazione ordine asporto ERRATA. Prestare attenzione !")
       msg.exec()
       with self.assertWarns(msg) as cm:
            vistaAggiungiOrdineAsporto.aggiungiOrdine()
