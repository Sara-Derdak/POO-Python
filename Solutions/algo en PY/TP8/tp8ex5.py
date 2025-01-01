from numpy import zeros
T=zeros(10000,int)
A=zeros(10000,int)

while True:
  print("donnez le nombre des esntiers ")
  n=int(input())
  if(n>=0 or n<10000):
    break
s=0
for i in range(n):
    print("donner la valeur ",i+1,"du premier tableau" )
    T[i]=int(input())

    print("donner la valeur ",i+1,"du deuxiéme tableau" )
    A[i]=int(input())
    
    s=s+T[i]*A[i]
print("le produit scalaire est",s)
    