import matplotlib.pyplot as plt
import numpy as np
from PySide6 import QtWidgets
from numpy import spacing

from RistoMatic.GestioneAmministrativa import StatisticheEconomiche
import datetime

class VistaGrafico():

#   1 Grafico
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
        plt.ylabel('Incasso (€)')
        plt.xlabel('Giorno')
        plt.title('Guadagno totale per giorno')
        plt.xticks(rotation=45)
        plt.show()




#   4 Grafici
    def graficoStatisticheGestionali(self,ordiniAsporto,ordiniTavolo):

        fig, axes = plt.subplots(nrows=2, ncols=2)
        plt.tight_layout()


#   Plotto il diagramma a blocchi: N°COMANDE TAVOLI AL GIORNO:
        giorni = []
        for sgiorno in ordiniTavolo.keys():  # I giorni vanno bene per tutti e quattro i grafici
           # dataSporca = sgiorno.isoformat()
            dataPulita = datetime.date(sgiorno.year,sgiorno.month,sgiorno.day).strftime('%m-%d')
            giorni.append(dataPulita)
        numComandeTavolo = []
        for value in ordiniTavolo.values():
            numComandeTavolo.append(len(value))

        x_pos = np.arange(len(giorni))
        plt.bar(x_pos, numComandeTavolo, align='center')
        plt.xticks(x_pos, giorni)
        plt.ylabel('n° com. tavoli')
        plt.xlabel('Giorno')
        plt.title('n°com. tavoli X giorno')
        plt.xticks(rotation=45)
        plt.plot(plt.bar)
        plt.show()






#   Grafi


