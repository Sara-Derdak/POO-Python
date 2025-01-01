class CompteBancaire:
    
    def __init__(self, solde=0):
        self.__solde = solde
        
    def get_solde(self):
        return self.__solde
    def set_solde(self,s):
        if s>0 :
            self.__solde = s

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        self.solde -= montant
        
    def __str__(self):
        return f"le solde est : {self.__solde}"


class CompteEpargne(CompteBancaire):
    def __init__(self, solde=0, taux_interet=0):
        super().__init__(solde)
        self.__taux_interet = taux_interet

    def calculer_interets (self):
        I = self.__solde * self.__taux_interet
        return I


class ComptePayant(CompteBancaire):
    def __init__(self, solde=0):
        super().__init__(solde)

    def deposer(self, montant):
        super().deposer(montant - 1)

    def retirer(self, montant):
        super().retirer(montant + 1)



C1 = CompteBancaire()
C1.deposer(100)
C1.retirer(30)
print(C1)

C2 = CompteEpargne(500,0.05)
C2.calculer_interets()



C3 = ComptePayant(solde=200)
C3.deposer(50)
C3.retirer(25)
print(C3)

