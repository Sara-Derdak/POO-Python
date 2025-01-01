def log_cible(L,log):
    chaine=[]
    for x in L :
        if len(x)==log :
            chaine.append(x)
    return chaine


chaine=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=input()
    chaine.append(a)
log=int(input("Donner la longueur : "))
print(chaine)
print("la nouvelle liste est : ",log_cible(chaine,log))
