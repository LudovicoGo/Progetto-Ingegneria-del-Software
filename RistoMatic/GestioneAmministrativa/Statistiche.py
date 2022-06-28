from abc import abstractmethod
from RistoMatic.GestioneAmministrativa import StatisticheEconomiche
import datetime

class Statistiche():


    def __init__(self,inizioCampionamento,fineCampionamento):
        self.dataInizio = inizioCampionamento
        self.dataFine = fineCampionamento


    def getDataFine(self):
        return self.dataFine

    def getDataInizio(self):
        return self.dataInizio

    def setDataInizio(self , setInizio):
        self.dataInizio = setInizio

    def setDataFine(self , setFine) :
        self.dataFine = setFine

    @abstractmethod
    def calcolaStatistiche(self)-> dict:
        return


    @abstractmethod
    def generaStatistiche(self)->dict:
        return


     # TODO LUCA : rifinire meglio l'esportazione
    def esportaStatistiche(self):
        file_object = open("Dati/Statistiche.txt", 'a')
        file_object.write('Data : ' + datetime.datetime.now() + '\n' + '\n' + '\n')
        if isinstance(self,StatisticheEconomiche):
            file_object.write("Statistiche economiche:")
            file_object.write(self.generaStatistiche())
        elif isinstance(self,StatisticheEconomiche):
            file_object.write('Statistiche gestionali: ')
            file_object.write(self.generaStatistiche())










