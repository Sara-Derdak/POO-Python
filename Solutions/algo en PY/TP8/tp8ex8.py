from numpy import zeros
T=zeros((1000,1000),int)

while True:
  print("donnez le nombre des lignes ")
  n=int(input())
  print("donnez le nombre des colonnes ")
  m=int(input())
  if(n>=0 or n<1000 or m>=0 or m<1000):
    break
for i in range(n):
    s=0
    for j in range(m):
      print("donner la valeur de la ligne",i+1)
      T[i][j]=int(input())
      s=s+T[i][j]
    print("la somme de la ligne",i+1,"est",s)
    print("la moyenne de la ligne",i+1,"est",s/m)
for i in range(m):
    s=0
    for j in range(n):
      print("donner la valeur de la colonne",i+1 )
      T[i][j]=int(input())
      s=s+T[i][j]
    print("la somme de la colonne",i+1,"est",s)
    print("la moyenne de la colonne",i+1,"est",s/n)