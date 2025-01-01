from numpy import zeros
T=zeros(10000,int)
A=zeros(10000,int)
while True:
  print("donnez le nombre des esntiers ")
  n=int(input())
  if(n>=0 or n<10000):
    break
for i in range(n):
    print("donner la valeur ",i+1,"du premier tableau" )
    T[i]=int(input())
for j in range(n):
    print("donner la valeur ",j+1,"du deuxiéme tableau" )
    A[j]=int(input())
m=True
for k in range(0,n):
    if(T[k]!=A[k]):
        m=False
if(m==True):
    print("les tableaus sont identiques")
else:
    print("les tableaus ne sont pas identiques")