def concatination(chaine):
    R=""
    for x in chaine :
        R=R+x+" "
    return R


chaine=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=input()
    chaine.append(a)
print(chaine)
print("la nouvelle liste : ",concatination(chaine))
