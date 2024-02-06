from math import sqrt
class Piramida:
    def __init__(self, _a, _h) -> None:
        self.a = _a
        self.h = _h
        self.pp = _a ** 2 + 2 * _a * (sqrt((_a / 2) ** 2 + _h ** 2))
        self.ob = (_a ** 2 * _h) / 3

    def zmien(self, a, h):
        self.a = a
        self.h = h
        self.pp = a ** 2 + 2 * a * (sqrt((a / 2) ** 2 + h ** 2))
        self.ob = (a ** 2 * h) / 3

    def inf(self):
        print("Piramida:")
        print("Pole powierzchni:", self.pp)
        print("Objętość:", self.ob)


pyramid = Piramida(4, 5)
pyramid.zmien(6, 7)
pyramid.inf()