from numpy import zeros
T=zeros((1000,1000),int)

while True:
  print("donnez le nombre des lignes ")
  n=int(input())
  print("donnez le nombre des colonnes ")
  m=int(input())
  if(n>=0 or n<1000 or m>=0 or m<1000):
    break
s=0
for i in range(n):
    for j in range(m):
      print("donner la valeur ",i+1, )
      T[i][j]=int(input())
      s=s+T[i][j]
M=s/n*m
print("la somme des éléments de tableau est",s)
print("la moyenne des éléments du tableua est",M)
