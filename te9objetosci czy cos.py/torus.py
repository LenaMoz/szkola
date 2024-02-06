from math import pi
class Torus:
    PI = pi

    def __init__(self, _R, _r) -> None:
        self.R = _R
        self.r = _r
        self.pp = 4 * Torus.PI ** 2 * _R * _r
        self.ob = 2 * Torus.PI ** 2 * _R ** 2 * _r

    def zmien(self, R, r):
        self.R = R
        self.r = r
        self.pp = 4 * Torus.PI ** 2 * R * r
        self.ob = 2 * Torus.PI ** 2 * R ** 2 * r

    def inf(self):
        print("Torus:")
        print("Pole powierzchni:", self.pp)
        print("Objętość:", self.ob)

torus = Torus(5, 2)
torus.zmien(8, 3)
torus.inf()