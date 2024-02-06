from math import pi

class Walec: 
    PI = pi
    def __init__(self, _r, _h) -> None:
        self.r = _r
        self.h = _h
        self.pp = 2*Walec.PI*_r*_h + 2*Walec.PI*_r**2
        self.ob = Walec.PI*_r**2*_h

    def zmien(self,r,h):
        self.r = r
        self.h = h
        self.pp = 2*Walec.PI*r*h + 2*Walec.PI*r**2
        self.ob = Walec.PI*r**2*h

    def inf(self):
        print(self.pp)
        print(self.ob)

bb = Walec(32,2)
bb.zmien(21,21)
bb.inf()