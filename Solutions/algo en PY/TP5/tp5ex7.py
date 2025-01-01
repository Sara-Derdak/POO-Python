print("entrez votre entier")
e=int(input())
if(e<0):
    print("erreur,ce nombbre est négatif")
else:
    print("les diviseurs de ",e,"sont :")
    for i in range(1,e+1):
        if(e%i==0):
            print(i)