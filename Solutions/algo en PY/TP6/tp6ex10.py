def somme_chifres(e):
    m=e//1000
    c=(e%1000)//100
    d=(e%100)//10
    s=m+c+d
    return s

print("entrez votre entier ")
e=int(input())
s=somme_chifres(e)
print("la somme des chiffres est :" ,s)