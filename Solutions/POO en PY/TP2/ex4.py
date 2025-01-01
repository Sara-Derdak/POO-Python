class Produit :
    __total_prodits_vendus= 0
    def __init__(self,N='Inconnue',P='Inconnue',Q='Inconne'):
        self.__nom=N
        self.__prix=P
        self.__quantite_stock=Q
        
    @property
    def nom (self):
        return self.__nom
    
    @nom.setter
    def nom (self,n):
        self.__nom = n
        
    @property
    def prix (self):
        return self.__prix
    
    @prix.setter
    def prix (self,p):
        self.__prix = p
        
    @property
    def quantite_stock (self):
        return self.__quantite_stock
    
    @quantite_stock.setter
    def quantite_stock (self,q):
        self.__quantite_stock = q
        
    def vendre_produit (self,q_specif):
        if q_specif <= self.quantite_stock and q_specif>0:
            self.quantite_stock = self.__quantite_stock - q_specif
            Produit.__total_prodits_vendus = Produit.__total_prodits_vendus + 1
        else:
            print("Quantité insuffisante en stock") 
    
    @ staticmethod 
    def afficher_total_vendus():
        print("Nombre total de produits vendus : ",Produit.__total_prodits_vendus)
        
    def afficher (self) :
        print(f"le nom de la produit : {self.__nom} sa quantite {self.__quantite_stock} et son prix {self.__prix}")

    
P1=Produit('Ali',2000,100)
print(P1.nom)
print(P1.prix)
P1.vendre_produit(10)
P1.afficher()
print(Produit.afficher_total_vendus())