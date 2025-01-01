def Paire_impaire(L):
    P=['liste des nombres paires ']
    I=['liste des nombres impaires']
    for x in L :
     if(x%2==0):
        P.append(x)
     else:
        I.append(x)
    return P,I


L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
print(L)
print(Paire_impaire(L))
# P=[]
# I=[]
# for x in L :
#     if(x%2==0):
#         P.append(x)
#     else:
#         I.append(x)