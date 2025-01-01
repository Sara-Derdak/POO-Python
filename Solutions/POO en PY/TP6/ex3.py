from abc import ABC,abstractmethod

class Ouvrage (ABC):
    code=0
    def __init__(self,t):
        self.__titre=t
        Ouvrage.code+=1
        self.__code=Ouvrage.code
        self.__nb_emp=0
        self.__etat=True
        
    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self,t):
        self.__titre=t  
    
        
      
    def get_code(self):
        return self.__code
    
  
    def get_nbemp(self):
        return self.__nb_emp
    
    
    @property
    def etat(self):
        return self.__etat
        
    @abstractmethod
    def emprunter(self):
        pass
    
    @abstractmethod
    def retourner(self):
        pass
    
    def __str__(self):
        return f"Le titre : {self.__titre} "
    
    
class Livre(Ouvrage):
    def __init__(self, t,a,e):
        super().__init__(t)
        self.__auteur=a
        self.__editeur=e
        
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self,a):
        self.__auteur=a
        
    def get_editeur(self):
        return self.__editeur
    def set_editeur(self,e):
        self.__editeur=e
        
    def emprunter(self):
      if self._etat == True :
        self._etat=False
        self.__nb_emp += 1
        print(f"Le livre ({self.titre()}, {self.__auteur}) a été emprunté avec succès")

      else :
        print(f"Le livre ({self.titre()}, {self.__auteur}) indisponible")
        
    def retourner(self):
        if self._etat == False :
            self._etat=True
            print(f"Le livre ({self.titre}, {self.__auteur}) a été restitué avec succès")
        else :
            print(f"Le livre ({self.titre}, {self.__auteur}) deja exciste")
            

    def __str__(self):
        return "Livre : " + super().__str__()+f"L'auteur : {self.__auteur}, L'editeur : {self.__editeur}"
    
    


class CD(Ouvrage):
    def __init__(self, t,a,n):
        super().__init__(t)
        self.__artiste=a
        self.__nbr=n
        # self.set__nbr(n)
        
    def get_artiste(self):
        return self.__artiste
    def set_artiste(self,a):
        self.__artiste=a
        
    @property    
    def nbr(self):
        return self.__nbr
    @nbr.setter
    def nbr(self,nbr):
        if nbr>0 :
            self.__nbr
        else:
            raise Exception ("Le nombre invalide")
        

    def emprunter(self):
      if self._etat == True :
        self._etat=False
        self.__nb_emp += 1
        print(f"Le CD ({self.titre()}, {self.__artiste}) a été emprunté avec succès")

      else :
        print(f"Le CD ({self.titre()}, {self.__artiste}) indisponible")
        
    def retourner(self):
        if self._etat == False :
            self._etat=True
            print(f"Le livre ({self.titre}, {self.__artiste}) a été restitué avec succès")
        else :
            print(f"Le livre ({self.titre}, {self.__artiste}) deja exciste")
        
        
        
    def __str__(self):
        return "Le CD :" + super().__str__()+f" L'artiste : {self.__artiste} . Le nombre de pistes : {self.__nbr}"
    
    
biblio=[Livre("TitreLivre1", "Auteur1", "Editeur1"), Livre("TitreLivre2", "Auteur1", "Editeur2"),CD("TitreCD1", "Artiste1", 10), CD("TitreCD2", "Artiste2", 15)] 
    
while True :
        print("       Menu :        ")
        print("1- Afficher tous les ouvrages.")
        print("2- Afficher les ouvrages disponibles seulement.")
        print("3- Afficher tous les Livres.")
        print("4- Afficher tous les CDs.")
        print("5- Afficher les auteurs de tous les livres.")
        print("6- Afficher les artistes de tous les CDs.")
        print("7- Ajouter un ouvrage (Livre ou CD) à la bibliothèque.")
        print("8- Supprimer un ouvrage (par code)")
        print("9- Modifier le titre d'un ouvrage")
        print("10- Rechercher un ouvrage par code. (Afficher également son type)")
        print("11- Rechercher un Livre par code ")
        print("12- Rechercher un CD par code.")
        print("13- Rechercher un ouvrage par titre.")
        print("14- Rechercher un CD par artiste.")
        print("15- Rechercher un Livre par auteur.")
        print("16- Afficher tous les ouvrages classés par type")
        print("17- Afficher les ouvrages triés par ordre croissant de nombres d'emprunt")
        print("18- Emprunter un ouvrage par code")
        print("19- Restituer un ouvrage par code")
        print("20- Quitter")
        n=int(input("Donner le nombre qui represente votre choix : "))

        if n==1 :
            if not biblio :
                print("Aucun ouvrage dans la bibliotheque.")
            else:
                for i in biblio :
                  print(i)
                  
        if n==2 :
            b=False
            for i in biblio :
                if i.etat :
                    print(i)
                    b=True
            if not b :
                print("vide")
                    
        if n==3 :
            livres = []
            for i in biblio :
                if isinstance(i, Livre):
                    livres.append(i)
            if not livres:
                print("Aucun livre dans la bibliotheque.")
            else:
                for i in livres:
                    print(i)
                    
        if n==4:
            cds = []
            for i in biblio :
                if isinstance(i,CD):
                    cds.append(i)
            if not cds:
                print("Aucun CD dans la bibliotheque.")
            else:
                for i in cds:
                    print(i)
                    
        if n==5 :
            auteurs = []
            for i in biblio:
                if isinstance(i, Livre):
                    if i.get_auteur() not in auteurs :
                       auteurs.append(i.get_auteur())
            if not auteurs:
                print("Aucun auteur dans la bibliotheque.")
            else:
                for i in auteurs:
                    print(i)
                    
        if n==6 :
            artistes = []
            for i in biblio:
                if isinstance(i, CD):
                    if i.get_artiste() not in artistes :
                       artistes.append(i.get_artiste())
            if not artistes:
                print("Aucun artiste dans la bibliotheque.")
            else:
                for i in artistes:
                    print(i)
                    
        if n==7 :
            while True :
                t= input("Entrez le type d'ouvrage (Livre/CD): ").lower()
                titre=input("Entrez le titre de l'ouvrage: ")
                if t == "livre" or t == "cd" :
                    break
            if t == "livre":
                auteur = input("Entrez le nom de l'auteur : ")
                editeur = input("Entrez le nom de l'editeur : ")
                biblio.append(Livre(titre, auteur, editeur))
                print("Le livre ajoute avec succes.")

            elif t == "cd":
                artiste = input("Entrez le nom de l'artiste : ")
                nombre_pistes = int(input("Entrez le nombre de pistes : "))
                biblio.append(CD(titre, artiste, nombre_pistes))
                print("Le CD ajoute avec succes.")
        
        if n==8 :
           c=int(input("Entrez le code de l'ouvrage : "))
           b=False
           for i in biblio :
               if i.get_code() == c :
                  biblio.remove(i)
                  b=True
                  break
           if not b :
               print("Ouvrage introuvable.")
               
        if n==9 :
            c = int(input("Entrez le code de l'ouvrage a modifier: "))
            t = input("Entrez le nouveau titre de l'ouvrage: ")
            for i in biblio:
                b = False
                if i.get_code() == c:
                    i.titre = t
                    print(f"Le titre  modifie avec succes.")
                    b = True
                    break
                if b == False:
                    print("Ouvrage introuvable.")
                    
        if n==10 :
            b = False
            c= int(input("Entrez le code : "))
            for i in biblio:
                if i.get_code() == c:
                    if isinstance(i,Livre):
                       print("il s'agit d'un livre")
                    else :
                       print("il s'agit d'un CD")
                    b = True
                    break
                if b == False:
                    print("Ouvrage introuvable .")
            
        if n==11 :
            c = int(input("Entrez le code du livre : "))
            b = False
            for i in biblio:
                
                if isinstance(i, Livre) and i.get_code() == c:
                    print(i)
                    b = True
                    break
            if b == False:
                print("Livre introuvable.")
        
        if n==12 :
            c = int(input("Entrez le code du CD : "))
            b = False
            for i in biblio:                
                if isinstance(i, CD) and i.get_code() == c:
                    print(i)
                    b = True
                    break
            if b == False:
                print("CD non trouve.") 
                
        if n==13 :
            t = input("Entrez le titre : ")
            o = []
            for i in biblio:
                if i.t.lower() == titre.lower():
                    o.append(i)
            if not o:
                    print("Aucun ouvrage trouve avec ce titre.")
            else:
                    for i in o:
                        print(i)
                        
        if n==14 :
            a = input("Entrez le nom d'artiste du CD : ")
            cds = [] 
            for i in biblio:
                if isinstance(cd, CD): 
                    if cd.get_artiste().lower() == a.lower():
                        cds.append(cd)
            if not cds:
                print("n'exciste pas ce CD .")
            else:
                for cd in cds:
                    print(cd)
                    
        if n==15 :
            a = input("Entrez le nom d'auteur du Livre : ")
            livres = []
            for i in biblio:
                if isinstance(i, Livre):
                    if i.get_auteur().lower() == a.lower():
                        livres.append(i)
            if not livres:
                print("n'exciste pas ce livre.")
            else:
                for i in livres:
                    print(i)
                    
        if n==16 :
            livres = []
            cds = []
            for i in biblio:
                if isinstance(i, Livre):
                    livres.append(i)
                elif isinstance(i, CD):
                    cds.append(i)
            b=False
            print("Les Livres sont : ")
            for i in livres :
                print(i)
                b=True
            if b==False :
                print("n'exciste aucun livre ")
            b=False
            print("Les CDs sont : ")
            for i in cds :
                print(i)
                b=True
            if b==False :
                print("n'exciste aucun CD ")
                
        if n==17 :
            t = sorted(biblio, key=lambda x: x.get_nbemp(), reverse=True)
            print("Ouvrages tries :")
            for i in t:
                print(f"{i} - Nombre d'emprunts: {i.get_nbemp()}")
                
        if n==18 :
            c = int(input("entrer le code : "))
            b = False
            for i in biblio:
                if i.get_code() == c:
                    i.emprunter()
                    b = True
                    break
            if b == False:
                print("Ouvrage non trouve.")
                
        if n==19 :
            c= int(input("entrer le code :"))
            b = False
            for i in biblio:
                if i.get_code() == c:
                    i.restituer()
                    b = True
                    break
            if b == False:
                print("n'exciste aucun ouvrage.")
                
        if n==20 :
            print("Au revoir !")
            break
        
        v = input("voulez-vous continuer ?  (o/n) : ")
        if v.lower() != "o":
            break