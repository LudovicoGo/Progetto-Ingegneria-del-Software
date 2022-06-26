from abc import abstractmethod


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


    @abstractmethod
    def generaStatistiche(self)->dict:


    @abstractmethod
    def esportaStatistiche(self):
        # Magari si puo decidere di farle esportare in formato pdf o altri formati
        pass







