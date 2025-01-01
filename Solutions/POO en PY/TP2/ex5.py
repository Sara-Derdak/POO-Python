class Point :
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
    
    def get_x(self):
        return self.__x
    
    def set_x(self,x):
        self.__x=x
        
    def get_y(self):
        return self.__y
    
    def set__y(self,y):
        self.__y=y
        
    def afficher (self):
        print(f"POINT({self.__x},{self.__y})")
        
class Cercle :
    def __init__(self,p,r=0):
        self.__centre=p
        self.__rayon=r
        
    def getPerimetre (self):
        P=self.__rayon * 2 * 3.14
        return P
    
    def getSurface (self):
        S=self.__rayon * self.__rayon * 3.14
        return S 
    
    def Appartient (self ,a,b):
        if (((a - self.__centre.get_x())**2)+((b - self.__centre.get_y())**2) == self.__rayon):
            print(" la point p appartient au cercle") 
        else :
            print(" la point p n'appartient au cercle") 
        
    def Afficher (self):
        print(f"CERCLE({self.__centre.get_x},{self.__centre.get_y},{self.__rayonrayon})")
        
        

point1 = Point(2, 3)
point1.afficher()

cercle1 = Cercle(2,3,5)
print("Perimetre : ",cercle1.getPerimetre())
print("Surface : ",cercle1.getSurface())
cercle1.Appartient(2,4)
cercle1.Afficher()
