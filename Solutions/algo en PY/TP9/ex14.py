L=[]
L2=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
#     if(a%2==0):
#         L.append(0)
#     else:
#         L.append(1)
for i in L :
    if(i%2==0):
        L2.append(0)
    else:
        L2.append(1)
L=L2
print(L)