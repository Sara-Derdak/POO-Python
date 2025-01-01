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
    for j in range(m):
      print("donner la valeur de la ligne",i+1)
      T[i][j]=int(input())
min=T[0][0]
max=T[0][0]
for i in range(1,n):
    for i in range(1,m):
        if(min>T[i][j]):
            min=T[i][j]
        if(max<T[i][j]):
            max=T[i][j]
print("le max du tableau est ",max)
print("le min du tableau est ",min)
min=T[i][0]
max=T[i][0] 
for i in range(n):
    for j in range(m):
     if(min>T[i][j]):
        min=T[i][j]
    if(max<T[i][j]):
        max=T[i][j]
print("le max dans la ligne est ",max)
print("le min dans la ligne est ",min)