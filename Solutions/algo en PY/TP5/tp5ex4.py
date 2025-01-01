print("entrez votre nombre")
n=int(input())
if(n<3):
    print("doit entrer un nombre supérieur ou égal à 3")
else:
    print("les multiples de 3 qui se trouve entre 3 et",n,"sont")
    for i in range(3,n+1,3):
        print(i)


