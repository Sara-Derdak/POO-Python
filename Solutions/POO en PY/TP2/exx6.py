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
        print(f"Client {self.__nom} {self.__prenom} , CIN: {self.__CIN}, Tél: {self.__tele}")
        
class Compte :
    __nombre_comptes = 0
    def __init__(self,s='Inconnue',c='Inconnue',):   
        Compte.__nombre_comptes = Compte.__nombre_comptes + 1
        self.__proprietaire = c
        self.__solde=s
        self.__numCompte = Compte.__nombre_comptes
     
    def get_proprietaire(self):
        return self.__proprietaire
    
    def set__proprietaire(self,proprietaire):
        self.__proprietaire =  proprietaire    
     
    @property
    def num(self):
        return self.__numCompte 
    
    @property
    def solde(self):
        return self.__solde

    def crediter(self, somme):
        self.__solde = self.__solde + somme
        
    def debiter(self, somme):
        if somme <= self.__solde:
            self.__solde = self.__solde - somme
        else:
            print("Solde insuffisant.")
            
    def afficher_resume(self):
        print(f"Résumé du compte {self.__numCompte} - Solde : {self.__solde} DH - Propriétaire : {self.__proprietaire.nom()} {self.__proprietaire.prenom()}")
            
    @staticmethod
    def afficher_nombre_comptes():
        print(f"Nombre total de comptes créés : {Compte.__nombre_comptes}")
        

client1 = Clients("Ali1234", "Ali", "Ahmed", "0706000000")
client1.afficher()

compte1 = Compte(client1, 1000)

print(compte1.solde)

