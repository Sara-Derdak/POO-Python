def diviseurs(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)

print("entrez votre entier")
n=int(input())
print("la liste des diviseures :")
diviseurs(n)