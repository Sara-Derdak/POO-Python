def premier(e):
    p=0
    for i in range(1,e+1):
        if(e%i==0):
            p=p+1
    return p

e=int(input("entrez votre entier"))
p=premier(e)
if(p==2):
    print("le nombre est premier")
else:
    print("le nombre est non premier")