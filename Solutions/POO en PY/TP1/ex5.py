class CompteBancaire :
    def __init__(self,T='Inconnue',S='Inconnue'):
        self.titulaire=T
        self.sold=S
    def Afficher_infos(self):
        print("Le nom du titulaire est : ",self.titulaire,)
        print("Le solde du compte est : ",self.sold,"dh")

    def Montant(self,m):
        self.sold=self.sold+m
        
    def S_Montant(self,sm):
        if(self.sold>sm):
            self.sold=self.sold-sm
           
            
T=input("donner le nom du titulaire est : ")
# S=int(input("donner le solde du compte est : "))           
# m=int(input("Donner le Montant qui s'ajoute : "))
# ms=int(input("Donner le Montant qui va retirer : "))
C1=CompteBancaire(T,10000)
C1.Montant(2000)
C1.S_Montant(500)
C1.Afficher_infos()

C2=CompteBancaire('Mohamed',20000)
C2.Montant(300)
C2.S_Montant(21000)
C2.Afficher_infos()
