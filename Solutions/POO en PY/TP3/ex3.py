import time
class Livre:
    
    def __init__(self,t,a,annee,d):
        self.__titre=t
        self.__auteur=a
        self.__annee=annee
        self.__disponible=d
        
    def get_titre(self):
        return self.__titre
    def set_titre(self,t):
        self.__titre=t
        
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self,a):
        self.__auteur=a
        
        
    def get_annee(self):
        return self.__annee
    def set_annee(self,a):
        if a > 0 :
          self.__annee=a
        else :
            print("Erreur!!")
            
            
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self,d):
        self.__disponible=d
        
        
    def check_dispo(self):
        if self.__disponible :
            return "disponible pour le moment"
        else:
            return "indisponible pour le moment"    
        
        
    def emprunter(self):
        if self.__disponible :
            self.__disponible=False
        else:
            print("ce livre est indisponible")
        
    def rendre(self):
       if self.__disponible == False :
           self.__disponible = True
    
    
    def __str__(self):
      return f"le livre {self.__titre} écrit par l'auteur {self.__auteur}, et publie en {self.__annee} et il est {self.check_dispo()}"
  
  
class LivreNumerique(Livre) :
    
    def __init__(self, t, a, annee,d,f):
        super().__init__(t, a, annee ,d)
        self.__format=f
        
    def get_format(self):
        return self.__format
    
    def convertir_format(self,f):
        print("converture en cours ...")
        self.__format=f
        time.sleep(2)
        print(f"convertir en {self.__format} fait en succees")
        
    def telecharger(self):
        print("telechargement en cours ...")
        time.sleep(3)
        print("telechargement terminee")
    
    def __str__(self):
        return super().__str__()+f" et leur formt est : {self.__format}"
    
    
    
L1=Livre("titre1","auteur1",2020,True)
print(L1)
print(L1.get_disponible())                  
L1.emprunter()
print(L1)

print("******************")

L2=LivreNumerique("titre2","auteur2",2002,True,"PDF")
print("le format de ce livre est : ",L2.get_format())
L2.convertir_format("EPUB")
print(L2)
L2.emprunter()
L2.rendre()
L2.telecharger() 