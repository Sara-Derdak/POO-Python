class CompteBancaire :
    __taux_interet=None
    
    def __init__(self,T='Inconnue',S=0):
        self.__titulaire=T
        self.__solde=S
        
    @staticmethod
    def definir_taux_interet (nouveau_taux):
        CompteBancaire.__taux_interet = nouveau_taux
    def get_taux_interet ():
        return CompteBancaire.__taux_interet 
    
    @property
    def titulaire (self):
        return self.__titulaire
    @titulaire.setter
    def titulaire (self,t):
        self.__titulaire = t
        
    @property
    def solde (self):
        return self.__solde
    @solde.setter
    def solde (self,s):
        if s > 0 :
          self.__solde = s
          
    def calculer_interets (self):
        I = self.__solde * CompteBancaire.__taux_interet
        # print(f"Interets calcules pour le compte de {self.__titulaire} : {I}")
        return I
        


C1=CompteBancaire('Ali', 3000)
print(CompteBancaire.get_taux_interet())
print(C1.titulaire)
C1.titulaire = 'Mohammed'
C1.solde = 30000
print(C1.titulaire)
print(C1.solde)
print()