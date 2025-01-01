def Plus_chere(L):
    maxprix= L[0].get("prix")
    for j in range (len(L)):
        if maxprix < L[j].get("prix"):
            maxprix=L[j].get("prix")
    v=[]
    for i in L :
        if L[i].get("prix")==maxprix :
           v.append(L[i])
    return v


L=[]
for i in range(3):
    voiture={
            "Matricule":input(f"donner matricule de voitur {i+1} : "),
            "Marque":input(f"donner la marque {i+1} : "),
            "Model":input(f"donner la Model {i+1} : "),
            "prix":float(input(f"donner le prix {i+1} : "))
        }
    L.append(voiture)



print("\n")
print("La liste des voitures est :")
for i in L :
    print(i)
     
print("\n")
print("Les informations sur la voiture la plus chere : ",Plus_chere(L))



#     matricul=input(f"Donner le matricule de la voiture {i+1} :  ")
#     marque=input(f"Donner la marque de la voiture {i+1} :  ")
#     modele=input(f"Donner le module de la voiture {i+1} :  ")
#     prix=float(input(f"Donner le prix de la voiture {i+1} :  "))
#     voiture["matricul"]=matricul
#     voiture["marque"]=marque
#     voiture["modele"]=modele
#     voiture["prix"]=prix