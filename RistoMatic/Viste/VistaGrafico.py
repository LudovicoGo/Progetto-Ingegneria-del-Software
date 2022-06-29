import matplotlib.pyplot as plt
import numpy as np
from PySide6 import QtWidgets
from RistoMatic.GestioneAmministrativa import StatisticheEconomiche
import datetime

class vistaGrafico(QtWidgets.QWidget):

    def graficoStatisticheEconomiche(self,datiRaffinati):

        giorni = []
        for sgiorno in datiRaffinati.keys():
           # dataSporca = sgiorno.isoformat()
            dataPulita = datetime.date(sgiorno.year,sgiorno.month,sgiorno.day)
            giorni.append(dataPulita)




        plt.bar(x_pos, popolazione, align='center')
        plt.xticks(x_pos, citta)
        plt.ylabel('Popolazione')
        plt.xlabel('Citta')
        plt.title('Popolazione per citta')
        plt.show()

