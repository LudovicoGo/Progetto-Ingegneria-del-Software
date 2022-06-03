import sys
from PySide6 import QtWidgets
from random import *
from Viste.MainVistaMobile import VistaMobile
from Viste.MainVistaPreparazione import VistaPreparazione
from Viste.MainVistaSala import VistaSala
from GestioneAttivita.Tavolo import Tavolo
from GestioneAttivita.StatoSala import StatoSala

# main
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')

#generazione dati di esempio
    for i in range(0, 10):
        tavolo=Tavolo(randint(1,10))
        StatoSala.aggiungiTavolo(tavolo=tavolo)


    widgetPreparazione = VistaPreparazione()
    widgetPreparazione.resize(1280, 720)
    widgetPreparazione.show()

    widgetSala = VistaSala()
    widgetSala.resize(1280, 720)
    widgetSala.show()

    widgetMobile = VistaMobile()
    widgetMobile.resize(540, 640)
    widgetMobile.show()

    sys.exit(app.exec())