def somme(e):
    s=0
    for i in range(1,e+1):
        s=s+i
    return s
print("entrez votre entier")
e=int(input())
s=somme(e)
print("la somme est :",s)
    