print("entrez votre entier positif")
e=int(input())
if(e>0):
    s=0
    for i in range(0,e+1):
        s=s+i
    print("la somme des entiers entre 0 et",e,"est",s)
else:
    print("erreur")
