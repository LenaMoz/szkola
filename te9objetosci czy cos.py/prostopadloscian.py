class Prostopadloscian:
    def __init__(self, _a, _b, _c) -> None:
        self.a = _a
        self.b = _b
        self.c = _c
        self.pp = 2 * (_a * _b + _a * _c + _b * _c)
        self.ob = _a * _b * _c

    def zmien(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.pp = 2 * (a * b + a * c + b * c)
        self.ob = a * b * c

    def inf(self):
        print("Prostopadloscian:")
        print("Pole powierzchni:", self.pp)
        print("Objętość:", self.ob)

prostopadloscian = Prostopadloscian(2, 3, 4)
prostopadloscian.zmien(3, 4, 5)
prostopadloscian.inf()
