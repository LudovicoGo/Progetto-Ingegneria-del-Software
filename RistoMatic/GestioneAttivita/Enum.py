from enum import Enum

class Zone(Enum):
    CUCINA = 1
    BAR = 2
    FORNO = 3


class StatoComanda(Enum):
    NON_AVVIATA = 0
    AVVIATA = 1
    COMPLETATA = 2

class StatoTavolo(Enum):
    UTILIZZABILE =0
    OCCUPATO = 1
    PRENOTATO = 2