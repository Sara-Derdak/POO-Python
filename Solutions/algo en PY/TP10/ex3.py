chaine=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=input()
    chaine.append(a)
newchaine=[]
for x in chaine :
    if (len(x)>5):
        newchaine.append(x)
print("la nouvelle liste : ",newchaine)