class Produit :
    
    def __init__(self,n,p):
        self.__nom=n
        self.__prix=p
    
    def get_nom(self):
        return self.__nom
    def set_nom(self,n):
        self._nom=n
        
    def get_prix(self):
        return self.__prix
    def set_prix(self,p):
        if p>0 :
            self.__prix=p
        else :
            print("le prix invalide")
            
    def __str__(self):
        return f"le nom : {self.__nom} , le prix : {self.__prix}"
    
    def calcule_prix_final(self):
        return self.__prix
    
    
    

class Produit_electronique(Produit):
    
    def __init__(self, n, p,m,g):
        super().__init__(n, p)
        self.__marque=m
        self.__garantie=g
        
    def get_marque(self):
        return self.__marque
    def set_marque(self,m):
        self.__marque=m
        
    def get_garantie(self):
        return self.__garantie
    def set_garantie(self,d):
        if d>0:
            self.__garantie = d
        else :
            print("la duree est invalide")
    
    def prolonger_garantie(self,d):
        self.__garantie += d
        
    def __str__(self):
        return super().__str__()+f" la marque : {self.__marque} , et la duree du garantie est : {self.__garantie} mois"
    
    
class ProduitEnPromotion(Produit):
    
    def __init__(self, n, p, pr):
        super().__init__(n, p)
        self.__pourcentage_red=pr
        
    def get_pourcentage(self):
        return self.__pourcentage_red
    def set_pourcentage(self,pr):
        self.__pourcentage_red=pr
        
    def calcule_reduction(self):
        return self.get_prix() * (self.__pourcentage_red / 100)

    
    def calcule_prix_final(self):
        return super().calcule_prix_final() - self.calcule_reduction() 

    
    def __str__(self):
        return super().__str__() + f" et le pourcentage de reduction : {self.__pourcentage_red} "
    
    
    
P1=Produit("nom1",300)
print(P1)
print(P1.calcule_prix_final())

Pe=Produit_electronique("nom2",200,"marque2",3)
print(Pe.calcule_prix_final())
print(Pe)
Pe.prolonger_garantie(3)
print(Pe)

PP=ProduitEnPromotion("nom3",400,10)
print(PP)
print(PP.calcule_reduction())
print(PP.calcule_prix_final())