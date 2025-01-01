def Maj_Min(L):
    N=[]
    for x in L :
        if(len(x)%2==0):
            N.append(x.upper())
        else:
            N.append(x.lower())
    return N

T=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=input()
    T.append(a)
print(T)
print("la liste apres les modifications : " ,Maj_Min(T))