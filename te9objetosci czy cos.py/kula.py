from math import pi
class Kula:
    PI = pi

    def __init__(self, _r) -> None:
        self.r = _r
        self.pp = 4 * Kula.PI * _r ** 2
        self.ob = (4 / 3) * Kula.PI * _r ** 3

    def zmien(self, r):
        self.r = r
        self.pp = 4 * Kula.PI * r ** 2
        self.ob = (4 / 3) * Kula.PI * r ** 3

    def inf(self):
        print("Kula:")
        print("Pole powierzchni:", self.pp)
        print("Objętość:", self.ob)

kula = Kula(2)
kula.zmien(3)
kula.inf()      