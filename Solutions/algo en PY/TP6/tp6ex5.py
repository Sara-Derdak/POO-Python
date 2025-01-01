def paire(e):
    if(e%2==0):
        i=True
    else:
        i=False
    return i
e=int(input("entrez votre entier :"))
i=paire(e)
if(i==True):
    print("le nombre est paire")
else:
    print("le nombre est impaire")
    