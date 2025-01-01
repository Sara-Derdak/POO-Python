def supp(L):
    N=[]
    for x in L :
     if(x>0):
        N.append(x)
    return N

L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
print(L)
print("la nouvelle liste est : ",supp(L))