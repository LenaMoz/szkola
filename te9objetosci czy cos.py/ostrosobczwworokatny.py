from math import sqrt
class OstroslupCzworokatny:
    def __init__(self, _a, _b, _h) -> None:
        self.a = _a
        self.b = _b
        self.h = _h
        self.pp = _a * _b + 2 * ((_a + _b) / 2) * ((_a + _b) / 2 + sqrt((_b - _a) ** 2 / 4 + _h ** 2))
        self.ob = (_a * _b * _h) / 3

    def zmien(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        self.pp = a * b + 2 * ((a + b) / 2) * ((a + b) / 2 + sqrt((b - a) ** 2 / 4 + h ** 2))
        self.ob = (a * b * h) / 3

    def inf(self):
        print("Ostroslup Czworokatny:")
        print("Pole powierzchni:", self.pp)
        print("Objętość:", self.ob)


ostroslup_czworokatny = OstroslupCzworokatny(3, 4, 5)
ostroslup_czworokatny.zmien(4, 5, 6)
ostroslup_czworokatny.inf()
