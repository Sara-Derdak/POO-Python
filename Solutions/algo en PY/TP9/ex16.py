def list (L,n):
    LL=[]
    for i in L :
        p=i*n
        LL.append(p)
    L=LL
    return L

L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
print("entrez la valeur de multiplication")
n=int(input())
print(list(L,n))