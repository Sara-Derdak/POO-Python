def deplacement(L):
   T=[]
   for x in L :
       if(x==0):
           T.append(x)
           L.remove(x)
   T.extend(L)
   return T

L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
print(L)
print(deplacement(L))