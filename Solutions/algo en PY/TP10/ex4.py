def Reverse(T):
    B=[]
    for x in T :
        B.append(x[::-1])
    return B

T=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=input()
    T.append(a)
print(T)
print("la liste apres les modifications : " ,Reverse(T))