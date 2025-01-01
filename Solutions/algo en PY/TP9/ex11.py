L=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
L.reverse()
print(L)