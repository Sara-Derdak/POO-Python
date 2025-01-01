sp=0
sn=0
print("entez votre entier")
e=int(input())
while (e!=0):
    if(e>0):
        sp=sp+e
    elif(e<0):
        sn=sn+e
    print("entrez un entier")
    e=int(input())
print("la somme des valeurs positives est ",sp)
print("la somme des valeurs négatives est ",sn)