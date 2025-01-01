def occ_souschaine(L,s):
    n=0
    for x in L :
        if s in x :
           n=n+x.count(s)
    return n


L=['sara','bilal','souhaib','mohammed','hamid']
s=input("Donner la sous chaine : ")
print("le nombre d'occurences est : ",occ_souschaine(L,s))

