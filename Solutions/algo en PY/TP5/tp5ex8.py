e=int(input("enter  le nombre "))
s=0
if(e<0):
    print("entrez un nombre entier positif")
else:
    for i in range(1,e):
        if(e%i==0):
            s=s+i
    if(s==e):
        print("votre nombre est parfait")
    else:
        print("votre nombre n'est pas parfait")