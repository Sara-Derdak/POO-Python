from numpy import zeros
T=zeros(10000,int)
while True:
  print("donnez le nombre des esntiers ")
  n=int(input())
  if(n>=0 or n<10000):
    break
for i in range(n):
    print("donner la valeur ",i+1)
    T[i]=int(input())
print("donner une valeur")
x=int(input())
#p=-1
#for i in range (n):
 #   if(x==T[i]):
  #      p=i
   #     break
#if(p==-1):
 #   print(x,"n'excist pas dans le tableau")
#else:
 #   print(x,"exciste dans le tableau et sa position est : ",p+1)
 
for i in range(n):
    if(x==T[i]):
        print("exist,sa position est",i+1)
        break
         