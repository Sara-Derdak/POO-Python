L=[]
P=[]
I=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
for x in L:
    if(x%2==0):
        P.append(x)
    else:
        I.append(x)
print("la list principale est",L)
print("la liste des nombres paires est",P)
print("la liste des nombres impaires est",I)
