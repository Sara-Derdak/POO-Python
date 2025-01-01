L=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
LL=L.copy
L.reverse()
if(LL==L):
    print("la liste est palindrome")
else:
    print("la liste est non palindrome")