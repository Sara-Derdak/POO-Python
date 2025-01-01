from abc import ABC,abstractmethod

class Media(ABC):
    def __init__(self,t,e):
        self.__titre=t
        self.__emprunte=e
        
    def get_titre(self):
        return self.__titre
    def set_titre(self,t):
        self.__titre=t
    
    def get_emprunte(self):
        return self.__emprunte
    def set_emprunte(self,e):
        self.__emprunte=e
    
    def __str__(self):
        return f"Le titre du média est : {self.__titre}"

    @abstractmethod
    def emprunter(self):
        pass
    
    @abstractmethod
    def retourner(self):
        pass
    



class Livre(Media):
    def __init__(self, t, e , a , g):
        super().__init__(t, e)
        self.__auteur=a
        self.__genre=g
        
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self,a):
        self.__auteur=a

    def get_genre (self):
        return self.__genre 
    def set_genre (self,g):
        self.__genre =g
    
    def check_dispo(self):
        if self.get_emprunte() :
            return "disponible pour le moment"
        else:
            return "indisponible pour le moment"
        
    def __str__(self):
        return super().__str__()+f"L'auteur : {self.__auteur} , le genre :{self.__genre} et il est {self.check_dispo()}" 
    
    def emprunter(self):
        if self.get_emprunte() :
            self.set_emprunte(False)
            print(f"Le livre {self.get_titre()} écrit par {self.__auteur} a été emprunté avec succés")
            
    def retourner(self):
        if self.get_emprunte() == False:
            self.set_emprunte(True)
            print(f"Le livre {self.get_titre()} écrit par {self.__auteur} a été restitué avec succés")
            
            
class CD (Media):
    def __init__(self, t, e , a , d):
        super().__init__(t, e)
        self.__artiste=a
        self.__duree=d
        
    def get_artiste(self):
        return self.__artiste
    def set_artiste(self,a):
        self.__artiste=a
        
    def get_duree(self):
        return self.__duree
    def set_duree(self,d):
        if d > 0 :
            self.__duree=d
        else :
            print("la duree invalide")
        
        
    def check_dispo(self):
        if self.get_emprunte() :
            return "disponible pour le moment"
        else:
            return "indisponible pour le moment"
        
    def __str__(self):
        return super().__str__()+f" , L'artiste est {self.__artiste} , la duree : {self.__duree} jours , et il est {self.check_dispo()} "
    
    def emprunter(self):
        if self.get_emprunte() :
            self.set_emprunte(False)
            print(f"Le CD {self.get_titre()} , L'artiste {self.__artiste} a été emprunté avec succés")
            
    def retourner(self):
        if self.get_emprunte() == False:
           self.set_emprunte(True)
           print(f"Le CD {self.get_titre()} écrit par {self.__artiste} a été restitué avec succés")
            
            
            
l=Livre("livre1",True,"auteur1","genre1")
print(l)
l.emprunter()
print(l)
l.retourner()
print(l)

# cd=CD("cd1",True,"artiste1",7)
# print(cd)
# cd.emprunter()
# print(cd)
# cd.retourner()
# print(cd)
