class Applée_Etudiant :
    def __init__(self,N='Inconnue',M='Inconnue',C='Inconnue'):
        self.nom=N
        self.matricule=M
        self.cours=C
        self.notes=[]
        
    def Afficher_details(self):
        print("le nom est : ",self.nom)
        print("le matricule est : ",self.matricule)
        print("le nom du cours est : ",self.cours)
        
    def Ajouter_notes(self,c):
        self.notes.append(c)

    def calculer_notes(self):
        s=sum(self.notes)
        m=s/len(self.notes)
        return m

E1=Applée_Etudiant('ali','G1346839','algorithme')
E1.Afficher_details()
E1.Ajouter_notes()
M=E1.calculer_notes()
print("la moyenne est : ",M)


N=input("Donner votre nom : ")
M=input("Donner votre Matricule : ")
C=input("Donner le nom du cours : ")
E1=Applée_Etudiant(N,M,C)
E1.Afficher_details()
E1.Ajouter_notes()
M=E1.calculer_notes()
print("la moyenne est : ",M)