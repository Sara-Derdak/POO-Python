class Personne :
    def __init__(self,n,a,v):
        self.nom=n    
        self.age=a  
        self.ville=v 
    def afficher_details(self) :
        print("le nom est : ",self.nom," , lâge est : ",self.age," , et la ville est : ",self.ville)
        

n=input("Donner le nom: ")
a=int(input("Donner l'age: "))
v=input("Donner la ville : ")
P=Personne(n,a,v)
P.afficher_details()

PP=Personne('Mohamed',19,'Marrakech')
PP.afficher_details()