import matplotlib.pyplot as plt
import numpy as np
from PySide6 import QtWidgets
from numpy import spacing

from RistoMatic.GestioneAmministrativa import StatisticheEconomiche
import datetime

class VistaGrafico():

    def graficoStatisticheEconomiche(self,datiRaffinati):

        giorni = []
        for sgiorno in datiRaffinati.keys():
           # dataSporca = sgiorno.isoformat()
            dataPulita = datetime.date(sgiorno.year,sgiorno.month,sgiorno.day).strftime('%m-%d')
            giorni.append(dataPulita)


#       len(datiRaffinati.giorni)
        x_pos = np.arange(len(giorni))
        plt.bar(x_pos, datiRaffinati.values(), align='center')
        plt.xticks(x_pos, giorni)
        plt.ylabel('Incasso')
        plt.xlabel('Giorno')
        plt.title('Guadagno totale per giorno')
        plt.show()
        plt.subplots_adjust(bottom=200)

