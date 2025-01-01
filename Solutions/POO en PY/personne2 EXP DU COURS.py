 #création de la classe
class Personne:
    def __init__(self,n='sans',p='sans',a=0):        #constructeur d'initialisation et par défault
        self.nom=n    #initialisation des attributs
        self.prenom=p  #initialisation des attributs
        self.age=a            #initialisation des attributs
    def Sepresenter(self):     #définition d'une méthode (procédure)
        print("Je m'appelle ",self.nom,self.prenom, " et j'ai",self.age," ans")
    # def __del__(self):         #destructeur
    #     print("Objet supprimé")

n=input("Donner le nom: ")
p=input("Donner le prénom: ")
a=int(input("Donner l'age: "))

p1= Personne(n,p,a)                #instanciation
# p1.nom="Ahmedi"               #modification des attributs
# p1.prenom="Ali"
# p1.age=20
p1.Sepresenter()             #Appel de la méthode


p2=Personne("Mohamed","karim",30)
p2.Sepresenter()

p3=Personne()
p3.Sepresenter()
# p2=Personne()
# p2.Sepresenter()

