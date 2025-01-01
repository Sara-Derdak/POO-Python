from abc import ABC, abstractmethod
class Ouvrage(ABC):
    __code_ouvrage = 0
    def _init_(self, titre):
        Ouvrage.__code_ouvrage += 1
        self._code =Ouvrage._code_ouvrage 
        self.__titre = titre
        self.__disponible = True
        self.__nombre_emprunt = 0

    @property
    def code(self):
        return self.__code

    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self, titre):
        self.__titre = titre

    @property
    def disponible(self):
        return self.__disponible
    @disponible.setter
    def disponible(self, disponible):
        self.__disponible = disponible

    @property
    def nombre_emprunt(self):
        return self.__nombre_emprunt
    @nombre_emprunt.setter
    def nombre_emprunt(self, nombre_emprunt):  
        self.__nombre_emprunt = nombre_emprunt
    @staticmethod
    def get_code():
        return Ouvrage.__code_ouvrage
    @staticmethod
    
    @abstractmethod
    def emprunter(self):
        pass

    @abstractmethod
    def restituer(self):
        pass

    @abstractmethod
    def _str_(self):
        pass

class Livre(Ouvrage):
    def _init_(self, titre, auteur, editeur):
        super()._init_(titre)
        self._auteur = auteur
        self._editeur = editeur

    @property
    def auteur(self):
        return self._auteur

    @property
    def editeur(self):
        return self._editeur

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            self.nombre_emprunt += 1
            print(f"Le livre ({self.titre}, {self.auteur}) a ete emprunte avec succes.")
        else:
            print("le livre est pas disponible a le moment")
    def restituer(self):
        if not self.disponible:
            self.disponible = True
            print(f"Le livre ({self.titre}, {self.auteur}) a ete restitue avec succes.")
        else:
            print("le livre est deja disponible")
    def _str_(self):
        if self.disponible:
            c = "disponible"
        else:
            c = "pas disponible"
        return f"Livre {self.code}: {self.titre} - {self.auteur} - {self.editeur}, est {c} a le moment"

class CD(Ouvrage):
    def _init_(self, titre, artiste, nombre_pistes):
        super()._init_(titre)
        self._artiste = artiste
        self._nombre_pistes = nombre_pistes

    @property
    def artiste(self):
        return self._artiste

    @property
    def nombre_pistes(self):
        return self._nombre_pistes

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            self.nombre_emprunt += 1
            print(f"Le CD ({self.titre}, {self.artiste}, ) a ete emprunte avec succes.")
        else:
            print("le cd est pas disponible a le moment")

    def restituer(self):
        if not self.disponible:
            self.disponible = True
            print(f"Le CD ({self.titre}, {self.artiste}) a ete restitue avec succes.")
        else :
            print("le cd est deja disponible")

    def _str_(self):
        if self.disponible :
            c = "disponible"
        else:
            c= "pas disponible"
        return f"CD {self.code}: {self.titre} - {self.artiste} - {self.nombre_pistes} pistes est {c} a le moment"
def search(T, n):
    c = None
    for p in T:
        if p.code == n:
            c = p
            break
    return c
Bibliotheque = [Livre("titre1", "auteur1", "editeur1"), CD("titre2", "auteur2", 10)]
def menu_exercice3():

    while True:
        print("\nMenu Gestion de Bibliotheque:")
        print("1. Afficher tous les ouvrages.")
        print("2. Afficher les ouvrages disponibles seulement.")
        print("3. Afficher tous les livres.")
        print("4. Afficher tous les CDs.")
        print("5. Afficher les auteurs de tous les livres.")
        print("6. Afficher les artistes de tous les CDs.")
        print("7. Ajouter un ouvrage (Livre ou CD) a la bibliotheque.")
        print("8. Supprimer un ouvrage (par code).")
        print("9. Modifier le titre d'un ouvrage.")
        print("10. Rechercher un ouvrage par code. (Afficher egalement son type)")
        print("11. Rechercher un Livre par code.")
        print("12. Rechercher un CD par code.")
        print("13. Rechercher un ouvrage par titre.")
        print("14. Rechercher un CD par artiste.")
        print("15. Rechercher un Livre par auteur.")
        print("16. Afficher tous les ouvrages classes par type.")
        print("17. Afficher les ouvrages tries par ordre croissant de nombres d'emprunt.")
        print("18. Emprunter un ouvrage par code.")
        print("19. Restituer un ouvrage par code.")
        print("20. Quitter.")

        choice = int(input("Choisissez une option: "))

        if choice == 1:
            if not Bibliotheque:
                print("Aucun ouvrage dans la bibliotheque.")
            else:
                for ouvrage in Bibliotheque:
                    print(ouvrage)
        elif choice == 2:
            ouvrages_disponibles = []
            for ouvrage in Bibliotheque:
                if  ouvrage.disponible:
                    ouvrages_disponibles.append(ouvrage)
            if not ouvrages_disponibles:
                print("Aucun ouvrage disponible dans la bibliotheque.")
            else:
                for ouvrage in ouvrages_disponibles:
                    print(ouvrage)
        elif choice == 3:
            livres = []
            for ouvrage in Bibliotheque:
                if isinstance(ouvrage, Livre):
                    livres.append(ouvrage)
            if not livres:
                print("Aucun livre dans la bibliotheque.")
            else:
                for livre in livres:
                    print(livre)        
        elif choice == 4:
            cds = []
            for ouvrage in Bibliotheque:
                if isinstance(ouvrage, CD):
                    cds.append(ouvrage)
            if not cds:
                print("Aucun CD dans la bibliotheque.")
            else:
                for cd in cds:
                        print(cd)
        elif choice == 5:
            auteurs = []
            for livre in Bibliotheque:
                if isinstance(livre, Livre):
                    auteurs.append(livre.auteur)
            if not auteurs:
                print("Aucun auteur dans la bibliotheque.")
            else:
                print("Auteurs des livres:")
                for auteur in auteurs:
                    print(auteur)
        elif choice == 6:
            artistes = []
            for cd in Bibliotheque:
                if isinstance(cd, CD):
                    artistes.append(cd.artiste)
            if not artistes:
                print("Aucun artiste dans la bibliotheque.")
            else:
                print("Artistes des CDs:")
                for artiste in artistes:
                    print(artiste)
        elif choice == 7:
            type_ouvrage = input("Entrez le type d'ouvrage (Livre/CD): ").lower()
            titre = input("Entrez le titre de l'ouvrage: ")
            if type_ouvrage == "livre":
                auteur = input("Entrez le nom de l'auteur: ")
                editeur = input("Entrez le nom de l'editeur: ")
                Bibliotheque.append(Livre(titre, auteur, editeur))
                print("Ouvrage ajoute avec succes.")

            elif type_ouvrage == "cd":
                artiste = input("Entrez le nom de l'artiste: ")
                nombre_pistes = int(input("Entrez le nombre de pistes: "))
                Bibliotheque.append(CD(titre, artiste, nombre_pistes))
                print("Ouvrage ajoute avec succes.")

            else:
                print("Type d'ouvrage non reconnu.")
        elif choice == 8:
            code = int(input("Entrez le code de l'ouvrage a supprimer: "))
            # v = False
            # for ouvrage in Bibliotheque:
            #     if ouvrage.code == code:
            #         Bibliotheque.remove(ouvrage)
            #         print(f"L'ouvrage {ouvrage.titre} a ete supprime avec succes.")
            #         v = True
            #         break
            # if v == False:
            #     print("Ouvrage non trouve.")
            c = search(Bibliotheque, code)
            if c == None:
                print ("code n'existe pas")
            else :
                Bibliotheque.remove(c)
                print("Ouvrage supprime")
        elif choice == 9:
            code = int(input("Entrez le code de l'ouvrage a modifier: "))
            nouveau_titre = input("Entrez le nouveau titre de l'ouvrage: ")
            for ouvrage in Bibliotheque:
                v = False
                if ouvrage.code == code:
                    ouvrage.titre = nouveau_titre
                    print(f"Le titre de l'ouvrage {ouvrage.code} a ete modifie avec succes.")
                    v = True
                    break
                if v == False:
                    print("Ouvrage non trouve.")
        elif choice == 10:
            v = False
            code = int(input("Entrez le code de l'ouvrage a rechercher: "))
            for ouvrage in Bibliotheque:
                if ouvrage.code == code:
                    print(f"{ouvrage}\nType: {type(ouvrage)._name_}")
                    v = True
                    break
                if v == False:
                    print("Ouvrage non trouve.")
        elif choice == 11:
            code = int(input("Entrez le code du livre a rechercher: "))
            v = False
            for ouvrage in Bibliotheque:
                
                if isinstance(ouvrage, Livre) and ouvrage.code == code:
                    print(ouvrage)
                    v = True
                    break
            if v == False:
                print("Livre non trouve.")
        elif choice == 12:
            code = int(input("Entrez le code du CD a rechercher: "))
            v = False
            for ouvrage in Bibliotheque:                
                if isinstance(ouvrage, CD) and ouvrage.code == code:
                    print(ouvrage)
                    v = True
                    break
            if v == False:
                print("CD non trouve.")        
        elif choice == 13:
            titre = input("Entrez le titre de l'ouvrage a rechercher: ")
            ouvrages = []
            for ouvrage in Bibliotheque:
                if ouvrage.titre.lower() == titre.lower():
                    ouvrages.append(ouvrage)
            if not ouvrages:
                    print("Aucun ouvrage trouve avec ce titre.")
            else:
                    for ouvrage in ouvrages:
                        print(ouvrage)
        elif choice == 14:
            artistenom = input("Entrez le nom d'artiste du CD a rechercher: ")
            cds = [] 
            for cd in Bibliotheque:
                if isinstance(cd, CD): 
                    if cd.artiste.lower() == artistenom.lower():
                        cds.append(cd)
            if not cds:
                print("Aucun CD trouve avec cet artiste.")
            else:
                for cd in cds:
                    print(cd)
        elif choice == 15:
            at = input("Entrez le nom d'auteur du Livre a rechercher: ")
            livres = []
            for l in Bibliotheque:
                if isinstance(l, Livre):
                    if l.auteur.lower() == at.lower():
                        livres.append(l)
            if not livres:
                print("Aucun livre trouve avec cet auteur.")
            else:
                for livre in livres:
                    print(livre)
        elif choice == 16:
            # at = input("Entrez le nom d'auteur du Livre a rechercher: ")
            ouvrages_par_type = {}
            for ouvrage in Bibliotheque:
                type_ouvrage = type(ouvrage)._name_
                if type_ouvrage not in ouvrages_par_type:
                    ouvrages_par_type[type_ouvrage] = []
                ouvrages_par_type[type_ouvrage].append(ouvrage)

            for type_ouvrage, ouvrages in ouvrages_par_type.items():
                print(f"\n{type_ouvrage}s:")
                for ouvrage in ouvrages:
                    print(ouvrage)
        elif choice == 16:
            livres = []
            cds = []
            for ouvrage in Bibliotheque:
                if isinstance(ouvrage, Livre):
                    livres.append(ouvrage)
                elif isinstance(ouvrage, CD):
                    cds.append(ouvrage)

            print("\nLivres:")
            for livre in livres:
                print(livre)

            print("\nCDs:")
            for cd in cds:
                print(cd)

        elif choice == 17:
            ouvrages_tries = sorted(Bibliotheque, key=lambda x: x.nombre_emprunt, reverse=True)
            print("Ouvrages tries par nombre d'emprunts:")
            for ouvrage in ouvrages_tries:
                print(f"{ouvrage} - Nombre d'emprunts: {ouvrage.nombre_emprunt}")
        elif choice == 18:
            codeO = int(input("entrer le code de l'ouvrage a emprunter"))
            v = False
            for ouvrage in Bibliotheque:
                if ouvrage.code == codeO:
                    ouvrage.emprunter()
                    v = True
                    break
            if v == False:
                print("Ouvrage non trouve.")
        elif choice == 19:
            codeO = int(input("entrer le code de l'ouvrage a restituer"))
            v = False
            for ouvrage in Bibliotheque:
                if ouvrage.code == codeO:
                    ouvrage.restituer()
                    v = True
                    break
            if v == False:
                print("Ouvrage non trouve.")

        elif choice == 20:
            pass
        v = input("continuer? o/n : ")
        if v.lower() != "o":
            break
menu_exercice3()