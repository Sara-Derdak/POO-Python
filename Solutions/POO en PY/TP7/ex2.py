class Client:
    def __init__(self,c,n,p,a,t):
        self.__CIN=c
        self.__nom=n
        self.__prenom=p
        self.__adresse=a
        self.__tel=t

    @property
    def CIN (self):
        return self.__CIN
    @CIN.setter
    def CIN(self,c):
            self.__CIN=c
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n
        
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,p):
        self.__prenom=p
    
    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self,a):
        self.__adresse=a

    @property
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self,t):
        self.__tel=t

    def __str__(self):
        return f"Le client  {self.__nom , self.__prenom} a le CNE {self.__CIN} et le tel : {self.__tel}"
    

    
class Compte:
    __numero=0
    def __init__(self,s,t,c):
        Compte.__numero+=1
        self.__numero=Compte.__numero
        self.__solde=s
        self.type=t
        self.__client=c

    @property
    def solde(self):
        return self.__solde
    
    @property
    def numero(self):
        return self.__numero
    
    
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,t):
        if t=="C" or t=="E" : 
            self.__type=t
        else :
            raise Exception ("Type Invalide !!")
        
    @property
    def client(self):
        return self.__client
    @client.setter
    def client(self,c):
        self.__client=c
       

    def __str__(self):
        return f"numero de compte :{self.__numero} de client {self.__client} Le solde {self.__solde} le type {self.__type}"
    

class Banque:
    def __init__(self,n,s):
        self.__nomb=n
        self.__siege=s
        # self.__listecomptes=[]
        self.__listecomptes=[Compte(0,"E",Client("E1","nom1","prenom1","adr1","077744")),Compte(2000,"C",Client("E2","nom2","prenom2","a2","070944"))]

    @property
    def nomb(self):
        return self.__nomb
    @nomb.setter
    def nomb(self,n):
        self.__nomb=n

    @property
    def siege(self):
        return self.__siege
    @siege.setter
    def siege(self,n):
        self.__siege=n


    def __str__(self):
        c=""
        for i in self.__listecomptes :
            c=c+str(i)+"\n"
        return f"le nom Banque :{self.__nomb} Le siege :{self.__siege}  et la liste de comptes: {c}"
        # return f"le nom Banque :{self.__nomb} Le siege :{self.__siege} et la liste de comptes:\n {self.Returncomptes()}"


    def recherchercompte(self,n):
        for i in self.__listecomptes :
            if i.numero==n :
               return i
        return None
        

    def Ajoutercompte(self,compte):
      b=False
      self.__listecomptes.append(compte)
      if compte in self.__listecomptes :
        b=True
      return b
      
    def SupprimerCompte(self,n):
        b=self.recherchercompte(n)
        if b !=None :
            if  b.solde==0 :
                self.__listecomptes.remove(b)
                return True
        else:
            return False
    

    def Modifiertelclient(self,num,tel): 
        c=self.recherchercompte(num)
        if c==None :
            return False
        else :
            c.client.tel=tel
            return True
            

    def Returncomptes(self):
        return self.__listecomptes
        # for i in self.__listecomptes:
        #     print(i)

    def ReturncomptesE(self):
        L=[]
        for i in self.__listecomptes:
            if i.type=="E":
                L.append(i)
            return L

    def Returncomptesvaleurs(self,min,max):
        if min>max:
            m=min
            min=max
            max=m
        L=[]
        for i in self.__listecomptes:
            if  i.solde>min and i.solde<max :
                L.append(i)
        return L


    def Returncomptesclient(self,cin):    
        L=[]
        for i in self.__listecomptes :
            if i.client.CIN==cin :
                L.append(i)
        return L
    

    def comptemax(self):
        M=[]
        for i in self.__listecomptes:
            M.append(i.solde)
        L=[]
        for i in self.__listecomptes:
            if i.solde==max(M) :
                L.append(i)
        return L 
            
def Afficher(L):
    if len(L)>0 :
        for i in L :
            print(i)
    else :
            print("N'existe aucun compte")


b=Banque("BP","CASA")
while True :
    print("           Menu :           ")
    print("1-Ajouter un compte a la banque")
    print("2-Supprimer un compte ")
    print("3-Modifier le numero de telephone du client")
    print("4-Rechercher un compte")
    print("5-Afficher toutes les informations de la banque")
    print("6-Afficher toutes les comptes")
    print("7-Afficher toutes les comptes d'epargnes ")
    print("8-Afficher les comptes courants qui ont un solde entre deux valeurs donnees")
    print("9-Rechercher le(s) compte(s) a partir de son client")
    print("10-Afficher la somme de tous compts d'epagne dans la banque")
    print("11-Afficher la somme de tous compts d'un client dans la banque")
    print("12-Afficher les comptes ayant le solde maximal")
    print("13-Quitter")
    while True :
      n=int(input("Donner le nombre qui represnte l'operation qui vous voulez execute : "))
      if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9 or n==10 or n==11 or n==12 or n==13 :
        break
      else :
          print("Le nombre invalide , essaie une autre fois")
    
    if n==1 :
        s=float(input("Donner le solde"))
        t=input("Donner le type du compte (E/C) : ")
        cin=input("Donner le CIN du client : ")
        nom=input("Donner le nom du client : ")
        prenom=input("Donner le prenom du client : ")
        a=input("Donner l'adresse du client : ")
        tel=input("Donner le tel du client :")
        if b.Ajoutercompte(Compte(s,t,Client(cin,nom,prenom,a,tel)))==True :
            print("Le compte ajoutee avec succes")
        else :
            print("Erreur !! Verifier votre donnees et essaie une autre fois ")
    
    if n==2 :
        n=int(input("Donner le numero du compte : "))
        if b.SupprimerCompte(n)==True :
            print("Le compte supprime avec succes")
        else :
            print("Erreur !! , essaie une autre fois")

    if n==3 :
        n=int(input("Donner le numero du compte : "))
        if b.recherchercompte(n) != None :
           t=input("Donner le nouveau Tel : ")
           if b.Modifiertelclient(n,t)==True :
             print("La modification fait avec succes")
        else :
            print("Erreur !! Verifier votre donnees et essaie une autre fois ")
            
    if n==4 :
        n=int(input("Donner le numero du compte : "))
        a=b.recherchercompte(n)
        if a==None :
            print("Compte introuvable !!")
        else :
            print(a)

    if n==5 :
        print(b)

    if n==6:
        L=b.Returncomptes()
        Afficher(L)
        

    if n==7 :
        L=b.ReturncomptesE()
        Afficher(L) 

    if n==8 :
        min=float(input("Donner la 1er valeur : "))
        max=float(input("Donner la 2eme valeur : "))
        L=b.Returncomptesvaleurs(min,max)
        Afficher(L)   


    if n==9 :
        cin=input("Donner le CIN du client : ")
        L=b.Returncomptesclient(cin)
        Afficher(L)

    if n==10 :
       a=b.ReturncomptesE()
       s=0
       for i in a:
           s+=i.solde
       print(s)

   

    if n==11 :
        cin=input("Donner le CIN du client : ")
        a=b.Returncomptesclient(cin)
        s=0
        for i in a :
               s+=i.solde
        print("la somme de tous compts du client dans la banque est : ",s)
        


    if n==12 :
        L=b.comptemax()
        print("les comptes ayant le solde maximal : ")
        Afficher(L)
 

    if n==13 :
        print("Au revoire !!")
        break
        

    v=input("Voulez-vous continuer (o/n) ??   : ")
    if v=="n" or v=="N" :
        print("Au revoire !!")
        break


    
# c=Compte(2000,"E",Client("e3","ndm","323","wsd","38392"))
# print(c.client)