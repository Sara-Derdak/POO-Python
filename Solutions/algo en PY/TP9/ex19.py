def list3(L,T):
    C=[]
    for x in L :
        if x in T and x not in C :
            C.append(x)
    #LL=[]
    #for i in C:
    #  if i not in LL :
    #    LL.append(i)
    #C=LL
    return C

L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
print(L)
T=[]
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    T.append(a)
print(T)
C=list3(L,T)
print("la liste des éléments communs à ces deux listes est : ",C)     