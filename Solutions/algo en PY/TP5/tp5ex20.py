
s=0
while True:
    print("entrez votre entier")  
    e=int(input())
    s=s+e
    print("voulez vous ajouter un autre entier (o/n) :")
    c=input()
    if(c=="n" or c=="N"):
        break
print("somme des valeures est :",s)
