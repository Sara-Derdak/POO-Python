class Rectangle :
    def __init__(self,Log,Lag):
        self.Longueur=Log
        self.Largeur=Lag
        
    def Perimetre(self):
        P=2*(self.Longueur + self.Largeur)
        return P
    
    def Aire(self):
        A=(self.Largeur * self.Largeur)
        return A
    
    def EstCarre(self):
        if (self.Largeur == self.Longueur):
            return ("Il s'agit d'un carre")
        else:
            return("Il ne s'agit pas un carre")
    def Afficher(self):
        
        print(f"Longueur [{self.Longueur}] - Largueur [{self.Largeur}] - Perimetre [{self.Perimetre()}] - Aire [{self.Aire()}] - {self.EstCarre()}")

        
        
Log=float(input("donner la longuer de votre rectangle : "))
Lag=float(input("donner la largeure de votre rectangle : "))
R=Rectangle(Log,Lag)
print("le perimetre est : ",R.Perimetre())
print("L'aire de rectangle est : ",R.Aire())
R.Afficher()