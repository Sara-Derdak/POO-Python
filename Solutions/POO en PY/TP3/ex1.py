class Personne:
    
    def __init__(self,n='sans', a=0):      
        self.__nom=n    
        self.__age=a       
    
    def get_nom(self):
        return self.__nom
    def set_nom(self,n):
        self.__nom=n
        
    def get_age(self):
        return self.__age
    def set_age(self,a):
        if a > 0:
          self.__age=a
        else:
            print("Erreur!")
        
    def afficher_info(self):     
        print("Je m'appelle ",self.__nom," et j'ai",self.__age," ans",end="")
        
        
class Etudiant(Personne):
    
    def __init__(self, n='sans', a=0 , f='sans'):
        super().__init__(n , a)
        self.__filiere=f
        
    def get_filiere(self):
        return self.__filiere
    def set_filiere(self,f):
        self.__filiere=f
        
    def afficher_info(self):
        super().afficher_info()
        print(" et je suis un etudiant en filiere : ",self.__filiere)
        
        
        
        
class Employe(Personne):
    
    def __init__(self, n='sans', a=0 , p='sans'):
        super().__init__(n,a)
        self.__poste=p
        
    def get_poste(self):
        return self.__poste
    def set_poste(self,p):
        self.__poste=p
        
    def afficher_info(self):
        super().afficher_info()
        print(" et je suis employe et mon poste est : ",self.__poste)
        
        
        
        
p=Personne("Mohamed",23)
p.afficher_info()

print("\n")

et=Etudiant("Ahmed",20,"science physique")
et.afficher_info()

print("\n")

em=Employe("Karime",26,"Diricteur")
em.afficher_info()