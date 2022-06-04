from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLabel, QGridLayout, QLineEdit

from RistoMatic.Viste.Blocks.BlockComandaSala import BlockComandaSala
from RistoMatic.GestioneAttivita.Comanda import Comanda


class BlockDettaglioTavolo(QtWidgets.QWidget):

    def __init__(self,tavolo):
        super().__init__()
        self.setWindowTitle(f"Tavolo {tavolo.riferimentoTavolo}")
        self.tavolo=tavolo
        self.add=QPushButton("Crea comanda")
        self.add.clicked.connect(self.aggiungi_comanda)
        self.remove = QPushButton("Elimina comanda")
        self.remove.clicked.connect(self.rimuovi_comanda)
        self.stampa = QPushButton("Stampa preconto")
        self.stampa.clicked.connect(self.stampa_preconto)
        self.coperti = QLineEdit()
        self.coperti.setFixedSize(25, 25)
        self.coperti.textChanged.connect(self.modifica_coperti)
        self.coperti.setText(str(tavolo.getNumeroCoperti()))
        self.coperti.setAlignment(Qt.AlignLeft)
        self.lbl_coperti = QLabel("Coperti ")
        self.lbl_coperti.setAlignment(Qt.AlignRight)
        self.lbl_prenotazione = QLabel("Prenotazione: ")
        self.lbl_prenotazione.setAlignment(Qt.AlignRight)
        self.prenotazione = QLabel(str(tavolo.getNomeTavolo()))
        self.prenotazione.setAlignment(Qt.AlignLeft)

        self.comanda=Comanda.ricercaComanda(self.tavolo.riferimentoTavolo)
        self.wcomanda=None

        self.resize(540, 640)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.add,0,0,1,2)
        self.grid.addWidget(self.remove,0,1,1,2)
        self.grid.addWidget(self.lbl_coperti, 1, 0, 1, 1)
        self.grid.addWidget(self.coperti, 1, 1, 1, 1)
        self.grid.addWidget(self.lbl_prenotazione, 1, 2, 1, 1)
        self.grid.addWidget(self.prenotazione, 1, 3, 1, 1)
        self.grid.addWidget(self.stampa,3,0,1,4)

        if (not self.comanda == None):
            self.wcomanda = BlockComandaSala(self.comanda)
            self.grid.addWidget(self.wcomanda, 2, 0, 1, 4)

    def aggiungi_comanda(self):
        if self.comanda == None:
            self.comanda = Comanda(self.tavolo)
            self.wcomanda = BlockComandaSala(self.comanda)
            self.grid.addWidget(self.wcomanda, 1, 0, 1, 2)

    def rimuovi_comanda(self):
        self.wcomanda.deleteLater()
        self.comanda.rimuoviComanda()
        self.comanda = None

    def stampa_preconto(self):
        pass #manda i dati alla stampante

    def modifica_coperti(self):
        try:
            if not self.coperti.text() =="":
                self.tavolo.setNumeroCoperti(int(self.coperti.text()))
        except:
            print("Not int")
            self.tavolo.setNumeroCoperti(1)
            self.coperti.setText("1")