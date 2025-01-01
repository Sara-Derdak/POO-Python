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
D=[]
for x in L :
    if x not in T  and x not in D:
        D.append(x)
#for x in T :
#    if x not in L :
#        D.append(x)
print("la liste des éléments différents à ces deux listes est : ",D)  