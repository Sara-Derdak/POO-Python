print("entrez l'entier")
n=int(input())
f=1
if(n<0):
    print("erreur")
else:
    for i in range(n,1,-1):
     f=f*i
print("la facteriéle de",n,"est",f)