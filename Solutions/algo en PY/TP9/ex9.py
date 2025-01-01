L=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
   print("entrez la valeur ",i+1)
   a=int(input())
   L.append(a)
print("donnez un entier")
e=int(input())
for i in range(n):
   if(e==L[i]):
      print("la position est : ",i+1)
      break