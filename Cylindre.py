from Point import Point

class Cylindre:
    def __init__(self,x,y,r,h):
        self.h = h
        Point.__init__(self,x,y,r)

    def getVolume(self):
        return print(Point.getSurface(self) * self.h)

cylindre1 = Cylindre(0,0,9,43)

cylindre1.getVolume()