def multiples(n,m):
    for i in range(n,m+1):
        if(i%3==0):
            print(i)

print("entrez votre entier :")
n=int(input())
print("entrez votre entier :")
m=int(input())
print("les multiples de 3 qui se trouve entre ",n,"et",m,"sont")
multiples(n,m)