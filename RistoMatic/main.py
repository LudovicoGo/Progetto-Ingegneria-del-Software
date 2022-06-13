import sys
from PySide6 import QtWidgets

from RistoMatic.GestioneAttivita.Enum import Zone
from Viste.MainVistaMobile import VistaMobile
from Viste.MainVistaPreparazione import VistaPreparazione
from Viste.MainVistaSala import VistaSala
from GestioneAmministrativa.Menu import Menu
from GestioneAttivita.StatoSala import StatoSala
from GestioneAmministrativa.ElementoMenu import ElementoMenu

# main
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle('Fusion')

    widgetPreparazione = VistaPreparazione()
    widgetPreparazione.resize(1280, 720)
    widgetPreparazione.show()

    widgetSala = VistaSala()
    widgetSala.resize(1280, 720)
    widgetSala.show()

    widgetMobile = VistaMobile()
    widgetMobile.resize(540, 640)
    #widgetMobile.show()


    sys.exit(app.exec())