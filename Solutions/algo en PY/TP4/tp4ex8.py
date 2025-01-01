
print("entrez la valeur de a sachant que l'équa. écrit sous la forme ax+b")
a=int(input())
print("entrez la valeur de b")
b=int(input())
if(b==0):
    print("la solution d'équation est l'ensemble R")
elif(a!=0):
    print("la solution d'équation est :",-b//a)
else:
    print("la solution d'équation est l'ensemble vide ")
print("Au revoire")
