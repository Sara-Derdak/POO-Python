def factoriel(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
print("entrez votre entier ")
a=int(input())
p=factoriel(a)
print("entrez votre entier ")
b=int(input())
f=factoriel(b)
print("la factoriel de ",a,"est :",p)
print("la factoriel de ",b,"est :",f)