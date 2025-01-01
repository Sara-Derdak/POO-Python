print("entrez votre nombre")
n=int(input())
t=0
if(n>0):
    for i in range(2,n):
        if(n%i==0):
            t=1
    if(t==1):
        print("le nombre est non premiére")
    else:
        print("le nombre est premiére")
else:
    print("vous devez entrer un nombre positif")