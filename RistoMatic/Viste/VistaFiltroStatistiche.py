from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QLabel, QCalendarWidget


class VistaFiltroStatistiche(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()


        self.vLayout = QVBoxLayout()

        self.data = QCalendarWidget()
        self.data.clicked.connect(self.selezionaData)
        self.dataSelezionata = None

        self.dataInizioString = QLabel("Giorno inizio campionamento:")
        self.dataFineString = QLabel("Giorno fine campionamento:")

        self.vLayout.addWidget(self.dataInizioString)
        self.vLayout.addWidget(self.dataFineString)


    def selezionaData(self):
        self.dataSelezionata = self.data.selectedDate()

        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()






