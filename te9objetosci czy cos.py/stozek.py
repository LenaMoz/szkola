from math import pi
class Stozek:
    PI = pi

    def __init__(self, _r, _h) -> None:
        self.r = _r
        self.h = _h
        self.l = (self.r ** 2 + self.h ** 2) ** 0.5
        self.pp = Stozek.PI * _r * (self.r + self.l)
        self.ob = (1 / 3) * Stozek.PI * _r ** 2 * _h

    def zmien(self, r, h):
        self.r = r
        self.h = h
        self.l = (self.r ** 2 + self.h ** 2) ** 0.5
        self.pp = Stozek.PI * r * (r + self.l)
        self.ob = (1 / 3) * Stozek.PI * r ** 2 * h

    def inf(self):
        print("Stozek:")
        print("Pole powierzchni:", self.pp)
        print("Objętość:", self.ob)

stozek = Stozek(3, 4)
stozek.zmien(5, 7)
stozek.inf()