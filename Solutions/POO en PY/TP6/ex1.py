class InvalideCINException(Exception):
    pass

import time

class Stagiaire :
    def __init__(self,c,n,p,f,t):
        self.CIN=c
        self.__nom=n
        self.__prenom=p
        self.__filiere=f
        self.note=t
        
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
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filiere(self,f):
        self.__filiere=f
        
    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self,n):
        if isinstance(n,int) or isinstance(n,float) and  n>=0 and n<=20 :
            self.__note=n
        else:
            raise Exception("note must be between 0 and 20")
        
    @property
    def CIN (self):
        return self.__CIN
    @CIN.setter
    def CIN(self,c):
        if len(c)==7 and c[0].isalpha() and c[2:].isdigit() :
            self.__CIN=c
        else:
            raise InvalideCINException ("Le CIN est invalide")
        
        
    def __str__(self):
        return f"Le stagiaire : {self.__nom , self.__prenom} a le CIN : {self.__CIN} "
    
    
    
L=[Stagiaire("E123456","nom1","prenom1","dev",13),Stagiaire("EE12345","nom2","prenom2","dev",14),Stagiaire("E123458","nom3","prenom3","full stack",16)]
#L=[]


while True :
        while True:
            print("         Menu :      ")
            print("1-Afficher tous les stagiaires")
            print("2-Afficher les notes de tous les stagiaires")
            print("3-Afficher les stagiaires ayant une note superieure ou egale une note donne")
            print("4-Ajouter un stagiaire dont les informations sont entrees par l'utilisateur")
            print("5-Rechercher un stagiaire par CIN donne")
            print("6-Rechercher les stagiaires d'une filière donnèe")
            print("7-Supprimer un stagiairedont le CIN est entree par l'utilisateur")
            print("8-Quitter")
            try:
                n=int(input("Donner le nombre qui represente votre choix : "))
                if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 :
                 break
            except Exception as a:
                print(a)
        if n==1 :
          if len(L) > 0 :
            for i in L :
              print(i)
          else :
              time.sleep(1)
              print("La liste vide . Doit entrer au moins un stagiaire")
              time.sleep(1)
              
        elif n==2 :
            if len(L) > 0 :
             for i in L :
                print(i.note)
            else :
              time.sleep(1)
              print("La liste vide . Doit entrer au moins un stagiaire")
              time.sleep(1)
       
        elif n==3 :
            try:
             if len(L) > 0 :
                e=float(input("Donner un note : "))
                # for i in L :
                #     if i.note != e :
                #       print("votre note n'exciste pas ! ")
                
                for i in L :
                   if i.note >= e :
                    print(i)
             else :
              time.sleep(1)
              print("La liste vide , doit entrer au moins un stagiaire")
              time.sleep(1)
            except Exception as a:
                print(a)
                
                
        elif n==4 :
            try:
                c=input("Donner le CIN du stagiaire : ")
                n=input("Donner le nom du stagiare : ")
                p=input("Donner le prenom du stagiare : ")
                f=input("Donner son filiere : ")
                t=float(input("Donner sa note : "))
            except Exception as a :
                print(a)
            if len(L) > 0 :
                for i in L :
                    if i.CIN == c :
                        time.sleep(2)
                        print("le CIN est deja exciste")
                        time.sleep(1)
                        break
                if i.CIN != c :
                        L.append(Stagiaire(c,n,p,f,t))
                        time.sleep(2)
                        print("le stagiaire ajouter avec success")
                        time.sleep(1)
            else :
                L.append(Stagiaire(c,n,p,f,t))
                time.sleep(2)
                print("le stagiaire ajouter avec success")
                time.sleep(1)
                    
        elif n==5 :
            if len(L) > 0 :
                try :
                   c=input("Donner Le CIN : ")
                except Exception as a:
                    print(a)
                for i in L :
                    if i.CIN == c :
                        print(i)
                        break
                if i.CIN != c :
                    time.sleep(2)
                    print("Votre CIN n'exciste pas !! ")
                    time.sleep(1)
            else :
                time.sleep(2)
                print("La liste vide , doit entrer au moins un stagiaire")
                time.sleep(1)
                
                
        elif n==6 :
            if len(L) > 0 :
                try:
                  f=input("Dooner un filiere : ")
                except Exception as a :
                    print(a)
                for i in L :
                    if i.filiere == f :
                        print(i)
                if i.filiere != f :
                    time.sleep(2)
                    print("Votre filiere n'exciste pas !! ")
                    time.sleep(1)
            else :
                time.sleep(2)
                print("Doit entrer au moins un stagiaire")
                time.sleep(1)
                
        elif n==7 :
            if len(L) > 0 :
                try :
                   c=input("Donner Le CIN : ")
                except Exception as a:
                    print(a)
                for i in range(len(L)): 
                 if L[i].CIN != c :
                    time.sleep(2)
                    print("Votre CIN n'exciste pas !! ")
                    time.sleep(1)
                for i in range(len(L)) :
                    if L[i].CIN == c :
                        del(L[i])
                        print("bien")
                        break
            else :
                time.sleep(2)
                print("Doit entrer au moins un stagiaire") 
                time.sleep(1)
                
        if n==8 :
                print("Au revoire !! ")
                break
            

                    
                
                
            
            
                    
    