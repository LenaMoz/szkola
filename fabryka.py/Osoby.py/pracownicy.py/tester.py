from Main import pracownicy

class tester(pracownicy):
    def __init__(self, imie,zawod, wyplata ):
        super().__init__(imie, zawod, wyplata)
        self.zawod = zawod
