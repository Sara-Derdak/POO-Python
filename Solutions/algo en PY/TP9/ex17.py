def list2(L):
   M=[]
   L.sort()
   M.append(L[0])
   M.append(L[-1])
   return M 
    
    
L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
M=list2(L)
print(M)
