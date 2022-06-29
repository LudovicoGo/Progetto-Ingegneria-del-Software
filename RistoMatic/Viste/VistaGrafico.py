import matplotlib.pyplot as plt
import numpy as np
from PySide6 import QtWidgets
from RistoMatic.GestioneAmministrativa import StatisticheEconomiche
import datetime

class vistaGrafico():

    def graficoStatisticheEconomiche(self,datiRaffinati):

        giorni = []
        for sgiorno in datiRaffinati.keys():
           # dataSporca = sgiorno.isoformat()
            dataPulita = datetime.date(sgiorno.year,sgiorno.month,sgiorno.day)
            giorni.append(dataPulita)



        x_pos = np.arange(len(datiRaffinati.giorni))
        plt.bar(x_pos, datiRaffinati.values(), align='center')
        plt.xticks(x_pos, datiRaffinati.giorni)
        plt.ylabel('Incasso')
        plt.xlabel('Giorno')
        plt.title('Guadagno totale per giorno')
        plt.show()

