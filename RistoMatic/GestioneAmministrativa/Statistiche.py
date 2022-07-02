from abc import abstractmethod
#from RistoMatic.GestioneAmministrativa import StatisticheEconomiche
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
    def calcolaStatistiche(self):
        return


    @abstractmethod
    def generaStatistiche(self)->dict:
        return


     # TODO LUCA : rifinire meglio l'esportazione
    def esportaStatistiche(self):
        file_object = open("Dati/Statistiche.txt", 'a')
        file_object.write('Statistiche del : ')
        file_object.write(datetime.date.today().strftime('%d %b %Y '))
        file_object.write(str(self.generaStatistiche()))
        file_object.close()











