L=[]
li=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
T=[]
#print("entre le nombres qui vous voulez")
#n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    c=input()
    T.append(c)
for i in range(n):
    li.append(L[i])
    li.append(T[i])
print(li)