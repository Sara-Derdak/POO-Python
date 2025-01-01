import math
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def Norme(self):
        D=math.sqrt(self.x**2+self.y**2)
        return D

a=float(input("donner l'abscisse du votre point : "))
o=float(input("donner l'ordonné du votre point : "))
P1=Point(a,o)
# D=P1.Norme()
print("la distance est : ",P1.Norme())

P2=Point()
D=P2.Norme()
print("la distance est : ",D)
