class Clients :
    def __init__(self,C,N,P,T):
        self.__CIN=C
        self.__nom=N
        self.__prenom=P
        self.__tele=T
        
    @property
    def nom (self):
        return self.__nom
    
    @nom.setter
    def nom (self,n):
        self.__nom = n
        
    @property
    def prenom (self):
        return self.__prenom
    
    @prenom.setter
    def prenom (self,p):
        self.__prenom = p
        
    @property
    def CIN (self):
        return self.__CIN
    
    @CIN.setter
    def CIN (self,c):
        self.__CIN = c
        
    @property
    def tele (self):
        return self.__tele
    
    @tele.setter
    def tele (self,t):
        self.__tele = t
        
    def afficher(self):
        print(f"Client {self.__nom} {self.__prenom} (CIN: {self.__CIN}, Tél: {self.__tele})")
        
        
class Compte:
    __nombre_comptes = 0

    def __init__(self, proprietaire, solde=0):
        Compte.nombre_comptes =  Compte.__nombre_comptes + 1
        self.__code_compte = Compte.__nombre_comptes
        self.__solde = solde
        self.proprietaire = proprietaire

    @property
    def code_compte(self):
        return self.__code_compte

    @property
    def solde(self):
        return self.__solde

    def crediter(self, montant):
        self.__solde = self.__solde + montant
        print(f"Compte {self.code_compte} crédité de {montant} DH. Nouveau solde : {self.solde} DH.")

    def debiter(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
            print(f"Compte {self.code_compte} débité de {montant} DH. Nouveau solde : {self.solde} DH.")
        else:
            print("Solde insuffisant.")

    def afficher_resume(self):
        print(f"Résumé du compte {self.code_compte} - Solde : {self.solde} DH - Propriétaire : {self.proprietaire.Nom} {self.proprietaire.Prenom}")

    @staticmethod
    def afficher_nombre_comptes():
        print(f"Nombre total de comptes créés : {Compte.nombre_comptes}")



client1 = Clients("Ali1234", "Ali", "Ahmed", "0706000000")
client1.afficher()

compte1 = Compte(client1, 1000)
compte2 = Compte(client1, 500)

compte1.crediter(200)
compte1.debiter(50)
