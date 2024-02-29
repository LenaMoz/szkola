class Osoby:
    def __init__(self, imie,):
        self.imie = imie
class produkt:
    def __init__(self, rodzaj,nazwa):
        self.rodzaj = rodzaj
        self.nazwa = nazwa
class niewolnicy:
    def __init__(self, imie,):
        self.imie = imie


   
class pracownicy(Osoby):
    def __init__(self, imie,zawod, wyplata ):
        super().__init__(imie, zawod)
        self.zawod = zawod
        self.wyplata = wyplata

class sprzataczka(pracownicy):
    def __init__(self, imie, zawod, wyplata):
        super().__init__(imie, zawod, wyplata)        

class czarnuchy(niewolnicy):
    def __init__(self, imie):
        super().__init__(imie)

class klienci(Osoby):
    def __init__(self, imie,listazakupow ):
        super().__init__(imie, listazakupow)
        self.listazakupow = listazakupow
    def przedstaw_sie(self):
        return f"jestem{self.imie} i chce kupić {self.listazakupow}"

class Biedni(klienci):
    def __init__(self, imie, listazakupow):
        super().__init__(imie, listazakupow)

class Bogaci(klienci):
    def __init__(self, imie, listazakupow):
        super().__init__(imie, listazakupow)

class Inspektor(Bogaci):
    def __init__(self, imie, listazakupow):
        super().__init__(imie, listazakupow)

class Bilionerzy(Bogaci):
    def __init__(self, imie, listazakupow):
        super().__init__(imie, listazakupow)        

class tester(pracownicy):
    def __init__(self, imie,zawod, wyplata ):
        super().__init__(imie, zawod, wyplata)
        self.zawod = zawod




class cukierki(produkt):
    def __init__(self, rodzaj, nazwa):
        super().__init__(rodzaj, nazwa)

class lizaki (cukierki):
    def __init__(self, rodzaj, nazwa):
        super().__init__(rodzaj, nazwa)

class watacukrowa (cukierki):
    def __init__(self, rodzaj, nazwa):
        super().__init__(rodzaj, nazwa)

class chipsy(produkt):
    def __init__(self, rodzaj, nazwa):
        super().__init__(rodzaj, nazwa)

class CzokoChips(chipsy):
    def __init__(self, rodzaj, nazwa):
        super().__init__(rodzaj, nazwa)            
