from Main import Osoby

class pracownicy(Osoby):
    def __init__(self, imie,zawod, wyplata ):
        super().__init__(imie, zawod)
        self.zawod = zawod
        self.wyplata = wyplata
