class Livre :
    def __init__(self,T='Inconnue',A='Inconnue',P='Inconnue'):
        self.__titre=T
        self.__auteur=A
        self.set__prix(P)
        # self.__prix=P
        
    def get__titre(self):
        return self.__titre
    
    def set__titre(self,t):
       self.__titre = t
       
    def get__auteur(self):
        return self.__auteur
    
    def set__auteur(self,a):
       self.__titre = a
       
       
    def get__prix(self):
        return self.__prix
    
    def set__prix(self,p):
       if p>0 :
        self.__prix = p
       else:
           print("Le prix invalide")
    
    def afficher_details(self) :
        print("le nom du livre est ",self.__titre," , l'auteur ",self.__auteur,"et le prix est : ",self.__prix,"DH") 
        
    
livre1 = Livre('Mésirables','victor HUGO', 20)
livre1.afficher_details()

print(livre1.get__titre())

livre1.afficher_details() 
livre1.set__titre('Antigone')
livre1.afficher_details() 

print(livre1.get__auteur())
livre1.set__auteur('Jean Anouil')
livre1.afficher_details()

print(livre1.get__prix())
livre1.set__prix(30)
livre1.afficher_details()

# liv=Livre()
# liv.afficher_details()