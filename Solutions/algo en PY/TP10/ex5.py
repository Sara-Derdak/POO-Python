def sous_chaine (L,s):
    N=[]
    for x in L :
        if s in x :
            N.append(x)
    return N

T=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=input()
    T.append(a)
print("entrez la sous chaines ")
s=input()
print(T)
print("les chaines qui contient la sous chaines sont : " ,sous_chaine(T,s))