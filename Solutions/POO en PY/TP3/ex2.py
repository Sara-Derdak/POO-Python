class Employe:
    
    def __init__(self,n,s):
        self.__nom=n
        self.__salaire=s
        
    def get_nom(self):
        return self.__nom
    def set_nom(self,n):
        self.__nom=n
            
            
    def get_salaire(self):
        return self.__salaire
    def set_salaire(self,s):
        if s>0:
          self.__salaire=s
        else:
            print("le salaire invalide")
        
        
    def calcule_salaire_annuel(self):
        return self.__salaire*12
    
    
    def __str__(self):
         return f"Je m'appelle {self.__nom} et mon salaire est : {self.__salaire} dh"
        
        
        
        
class Diricteur(Employe):
    
    def __init__(self, n, s ,p ,num ):
        super().__init__(n, s)
        self.__prime=p
        self.__nombre_dactions=num
        
    def get_prime(self):
        return self.__prime
    def set_prime(self,p):
        if p>0 :
          self.__prime=p
        else:
            print("le prime invalide")
            
            
    def get_nombre_dactins(self):
        return self.__nombre_dactins
    def set_nombre_dactins(self,num):
        if num>0:
          self.__nombre_dactins=num
        else:
            print("le nombre invalide")
            
            
    def calcule_salaire_annuel (self):
        return super().calcule_salaire_annuel() + self.__prime
    
    
    def __str__(self):
        return super().__str__() +f" et je suis un diricteur et j'ai possede {self.__nombre_dactions} actions dans l'entreprise ."
        
        
e=Employe("Ali",3000)
print(e)
print("et mon salaire annuuel est : ",e.calcule_salaire_annuel())


d=Diricteur("Mohamed",10000,500,5)
print(d)
print("et mon salaire annuuel est : ",d.calcule_salaire_annuel())

