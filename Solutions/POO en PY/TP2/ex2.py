class vehicule :
    def __init__(self,M='inconnu',Mod='Inconnu',A='Inconnu'):
        self.__marque=M
        self.__modele=Mod
        self.annee=A
        
    @property
    def marque (self) :
        return self.__marque
    
    @marque.setter
    def marque (self,marq):
        self.__marque=marq
    
    @property
    def annee (self) :
        return self.__annee
    
    @annee.setter 
    def annee (self,a):
        if a>0 :
          self.__annee=a
        else:
            print("l'annee est invalide")
            
    @property
    def module (self) :
        return self.__modele
    @module.setter 
    def modele (self,mod):
        self.__modele=mod
        
        
    def afficher_details(self) :
        print("la marque est : ",self.__marque,"le modéle est : ",self.__modele,"et lânnée est : ",self.__annee) 
        
        
A=vehicule("marque1","modele1",2023)
A.afficher_details()
print("la marque est : ",A.marque)
A.marque='nouvelle marque'
print("la marque est : ",A.marque)