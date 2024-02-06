class Szescian:
    def __init__(self, _a) -> None:
        self.a = _a
        self.pp = 6 * _a ** 2
        self.ob = _a ** 3

    def zmien(self, a):
        self.a = a
        self.pp = 6 * a ** 2
        self.ob = a ** 3

    def inf(self):
        print("Szescian:")
        print("Pole powierzchni:", self.pp)
        print("Objętość:", self.ob)
        
szescian = Szescian(4)
szescian.zmien(5)
szescian.inf()