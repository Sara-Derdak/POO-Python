

L=[]
print("donnez un entier")
e=int(input())
for i in range(1,e+1):
        if(e%i==0):
         L.append(i)
print("la liste de diviseures est :")
print(L)