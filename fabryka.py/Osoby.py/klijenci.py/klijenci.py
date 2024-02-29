from Main import Osoby

class klienci(Osoby):
    def __init__(self, imie,listazakupow ):
        super().__init__(imie, listazakupow)
        self.listazakupow = listazakupow
    def przedstaw_sie(self):
        return f"jestem{self.imie} i chce kupić {self.listazakupow}"
