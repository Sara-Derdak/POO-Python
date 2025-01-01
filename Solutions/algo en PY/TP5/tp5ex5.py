print("entrez votre nombre ")
n=int(input())
s=0
if(n<0):
    print("erreur , ce nombre est négatif")
else:
    for i in range(1,n+1):
        if(i%2!=0):
            s=s+i
    print("la sommme des entiers impaires est ",s)

    