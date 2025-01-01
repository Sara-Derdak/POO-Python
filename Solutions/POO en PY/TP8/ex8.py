def search(L,nom):
    for i in L :
        if i.get("nom")==nom :
            return i
    return None


L=[]
produit1={"nom":"produit1","prix_unitaire":200,"quantite_stocke":30}
produit2={"nom":"produit2","prix_unitaire":400,"quantite_stocke":48}
L.append(produit1)
L.append(produit2)

while True :
    while True : 
        print("           Menu :            ")
        print("1-Ajouter un nouveau produit")
        print("2-Rechercher un produit en utilisant son nom ")
        print("3-Afficher la liste de tous les produits ")
        print("4-mettre a jour les informations d'un produit existant en utilisant son nom")
        print("5-Supprimer un produit de la liste en utilisant son nom")
        print("6-Quitter")
        n=int(input("Donner le nombre qui represente votre choix : "))
        if n==1 or n==2 or n==3 or n==4 or n==5 or n==6 :
            break
        else:
            print("Votre choix invalide essaie une autre fois ")

    if n==1 :
        nom=input("Donner le nom du produit : ")
        if search(L,nom) is None :
        # prix=float(input("Donner le prix unitaire du produit : "))
        # quantite=int(input("Donner la quantite du produit en stock :"))
            produit={
                "nom":nom,
                "prix_unitaire":float(input("Donner le prix unitaire du produit : ")),
                "quantite_stocke":int(input("Donner la quantite du produit en stock :"))
            }
            # produit={"nom":nom,"prix_unitaire":prix,"quantite_stocke":quantite}
            L.append(produit)
            print("Le produit ajoutee avec succes ")
        else:
            print("Ce nom deja existe !!")

    elif n==2 :
        nom=input("Donner le nom du produit : ")
        b=search(L,nom)
        if b==None :
            print("N'existe aucun produit")
        else :
            print(b)

    elif n==3 :
        if len(L)>0 :
            print("la liste de tous les produits : ") 
            for i in L :
                print(i)
        else :
            print("La liste des produits est vide")

    elif n==4 :
        nom=input("Donner le nom du produit : ")
        b=search(L,nom)
        if b!= None :
            while True :
                print(" 1-Modifier le nom \n 2-Modifier le prix \n 3-Modifier la qauntite en stock")
                m=int(input("Donner votre choix : "))
                if m==1 or m==2 or m==3 :
                    break
                else :
                    print("Choix invalide essaie une autre foix ")
            if m==1 :
                nomN=input("Donner le nouveau nom du produit : ")
                b["nom"]=nomN
                print("L'information modifie avec succes")

            elif m==2 :
                prixN=float(input("Donner le nouveau prix unitaire : "))
                b["prix_unitaire"]=prixN
                print("L'information modifie avec succes")

            else :
                quantiteN=int(input("Donner la nouvelle quantite du produit en stock :"))
                b["quantite_stocke"]=quantiteN
                print("L'information modifie avec succes")

        else :
            print("n'existe pas ce produit ") 

    elif n==5 :
        nom=input("Donner le nom du produit : ")
        b=search(L,nom)
        if b==None :
            print("n'existe pas ce produit ") 
        else :
            L.remove(b)
            print("Le produit est supprimer avec succes")

    elif n==6 :
        print("Au revoire !!")
        break

    v=input("Voulez-vous continuer (o/n) ??   : ")
    if v=="n" or v=="N" :
        print("Au revoire !!")
        break
                        



        