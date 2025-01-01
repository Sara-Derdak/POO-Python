class Stagiaire :
    def __init__(self,c,n,p):
        self.CNE=c
        self.__nom=n
        self.__prenom=p
        
    @property
    def CNE (self):
        return self.__CNE
    @CNE.setter
    def CNE(self,c):
            self.__CNE=c
    
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

    def __str__(self):
        return f"Le stagiaire  {self.__nom , self.__prenom} a le CNE {self.__CNE}"
    

class Groupe:
    def __init__(self,ng,f):
        self.__nomgroupe=ng
        self.__filiere=f
        self.__listestagiaire=[Stagiaire("G1","dssd","wd"),Stagiaire("G2","dssd","wd")]

    @property
    def nomgroupe(self):
        return self.__nomgroupe
    @nomgroupe.setter
    def nomgroupe(self,n):
        self.__nomgroupe=n

    @property
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filiere(self,f):
        self.__filiere=f

    def __str__(self):
        return f"Le groupe : {self.__nomgroupe} , Filiere : {self.__filiere}"
    

    def Menu(self):
        print("           Menu :           ")
        print("1-Rechercher un stagiaire")
        print("2-Verifier est ce qu'un stagiaire exsite dans le groupe par CNE")
        print("3-Verifier est ce qu'un stagiaire exsite dans le groupe par nom et prenom")
        print("4-Ajouter un stagiaire")
        print("5-Afficher la liste des stagiares")
        print("6-Retirer un stagiaire")
        print("7-Quitter")
    
    def search(self,c):
        b=None
        for i in self.__listestagiaire :
            if i.CNE==c :
                b=i
                break
        return b

    def rechercher_stagiaire(self,a):
        b=self.search(a)
        if b==None:
            return False
        else :
            return b
        
    def stagiaire_existe_cne(self,c):
        b=self.search(c)
        if b==None :
            return False 
        else :
            return True
        
    def stagiaire_existe_nom(self,n,p):
        b=False
        for i in self.__listestagiaire :
            if n==i.nom and p==i.prenom :
                b=True
                break
        return b
    
    def ajouter_stagiare(self,stagiaire):
        if self.search(stagiaire.CNE)==None and len(self.__listestagiaire)<25 :
            self.__listestagiaire.append(stagiaire)
            return True
        else :
            return False
    
    def afficher_stagiaire(self):
        for i in self.__listestagiaire :
            print(i)

    def retirer_stagiaire(self,c):
        b=self.search(c)
        if b==None :
           return False
        else :
            self.__listestagiaire.remove(b)
            return True



g=Groupe("Dev103","dev")
while True :
    g.Menu()
    while True :
      n=int(input("Donner le nombre qui represnte l'operation qui vous voulez execute : "))
      if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 :
        break
      else :
        print("nonbre invalide")
    if n==1 :
        c=input("donner le CNE : ")
        b=g.rechercher_stagiaire(c)
        if b == False:
            print("Le CNE n'existe pas")
        else :
            print(b)

    if n==2 :
        c=input("donner le CNE : ")
        b=g.stagiaire_existe_cne(c)
        if b == True:
            print("Le stagiaire existe dans ce groupe")
        else :
            print("Le stagiare n'existe pas")

    if n==3 :
        nom=input("donner le nom : ")
        prenom=input("donner le prenom : ")
        b=g.stagiaire_existe_nom(nom,prenom)
        if b == True:
            print("Le stagiaire existe dans ce groupe")
        else :
            print("Le stagiare n'existe pas")

    if n==4 :
        cne=input('donner le CNE : ')
        nom=input("donner le nom : ")
        prenom=input("donner le prenom : ")
        if g.ajouter_stagiare(Stagiaire(cne,nom,prenom))==True :
            print("le stagiaire ajoute avec succes")
        else :
            print("Erreur le CNE deja existe")

    if n==5 :
        g.afficher_stagiaire()

    if n==6 :
        c=input("donner le CNE : ")
        b=g.retirer_stagiaire(c)
        if b == True:
            print("Le stagiaire retirer avec succes")
        else :
            print("Le stagiare n'existe pas")

    if n==7 :
        print("Au revoire !!")
        break

    v=input("Voulez-vous continuer (o/n) ??   : ")
    if v=="n" :
        print("Au revoire !!")
        break
    # else :
    #     continue
    





# g.afficher_stagiaire()
# print(g.search(1))




    

# s=Stagiaire(1,"dssd","wd")
# print(s.CNE)