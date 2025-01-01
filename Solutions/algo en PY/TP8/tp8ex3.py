from numpy import zeros
T=zeros(10000,int)
sp=0
sn=0
while True:
  print("donnez le nombre des esntiers ")
  n=int(input())
  if(n>=0 or n<10000):
    break
for i in range(n):
    print("donner la valeur ",i+1)
    T[i]=int(input())
    if (T[i]>=0):
        sp=sp+T[i]
    else:
        sn=sn+T[i]
print("la somme des entiers positifs est",sp)
print("la somme des entiers négatifs est",sn)