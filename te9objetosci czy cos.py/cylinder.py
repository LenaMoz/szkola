from math import pi
class Cylinder:
    PI = pi

    def __init__(self, _r, _h) -> None:
        self.r = _r
        self.h = _h
        self.pp = 2 * Cylinder.PI * _r * (_r + _h)
        self.ob = Cylinder.PI * _r ** 2 * _h

    def zmien(self, r, h):
        self.r = r
        self.h = h
        self.pp = 2 * Cylinder.PI * r * (r + h)
        self.ob = Cylinder.PI * r ** 2 * h

    def inf(self):
        print("Cylinder:")
        print("Pole powierzchni:", self.pp)
        print("Objętość:", self.ob)

cylinder = Cylinder(3, 6)
cylinder.zmien(4, 8)
cylinder.inf()
