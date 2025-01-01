def order_alpha(L):
    return sorted(L,reverse=True)



L=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=input()
    L.append(a)
print("la liste aprés les modifications : ",order_alpha(L))