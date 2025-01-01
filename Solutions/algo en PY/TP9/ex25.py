L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
print(L)
T=[]
for x in L :
    if(x%2==0):
        # c="paire"
        T.append(x)
        T.append('paire')
    else:
        # c="impaire"
        T.append(x)
        T.append('impaire')
print(T)