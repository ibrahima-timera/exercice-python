from math import *
class Point:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def afficher(self):
        print("Point(",self.x,",",self.y,")")

    def getPerimetre(self):
        return pi*2*float(self.r)

    def getSurface(self):
        return pi*pow(float(self.r),float(2))

    def appartient(self,i,j):
            if (i-self.x)**2 + (j-self.y)**2 == self.r**2:
                return "les points appartiennent au cercle"
            else:
                return "Les points n'appartiennent pas au cercle"

    def afficherCercle(self):
        print("Cercle(",self.x,",",self.y,",",self.r,")")

"""
a=float(input("Donnez le 1 point"))
b=float(input("Donnez le 2 point"))
c=float(input("Donnez le rayon du cercle"))

point1 = Point(a,b,c)

point1.afficher()
print("Le perimetre du cercle est ",point1.getPerimetre())
print("La surface du cercle est ",point1.getSurface())



print("appartenance",point1.appartient(0,1))

point1.afficherCercle()"""