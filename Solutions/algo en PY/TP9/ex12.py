L=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
T=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(n):
    print("entrez la valeur ",i+1)
    a=int(input())
    T.append(a)
F=L+T
F.sort()
print(F)       