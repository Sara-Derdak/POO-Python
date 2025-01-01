from numpy import zeros
T=zeros(1000,int)
while True:
  print("donnez le nombre des esntiers ")
  n=int(input())
  if(n>=0 or n<1000):
    break

for i in range(n):
    print("donnez l'entier ",i+1)
    T[i]=int(input())
min=T[0]
for i in range(1,n):
    if (min>T[i]):
      min=T[i]
max=T[0]
for i in range (1,n):
    if (max<T[i]):
      max=T[i]
print("le max est ",max)
print("le min est ",min)