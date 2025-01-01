class Livre :
    def __init__(self,T='Inconnue',A='Inconnue'):
        self.titre=T
        self.auteur=A
    def afficher_details(self) :
        print("le nom du livre est ",self.titre,"et l'auteur ",self.auteur) 
        
    
T=input("Donner le titre: ")
A=input("Donner le nom de l'auteur: ")
livre1=Livre(T,A)
livre1.afficher_details() 

livre2=Livre()
livre2.afficher_details()          