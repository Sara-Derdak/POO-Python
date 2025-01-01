def somme_produit(n,m):
    s=0
    p=1
    nm=0
    for i in range(n,m+1):
        if(i%2==0):
          nm=n+1
          s=s+i
          p=p*i
    print("la somme  des entiers paires est :",s)
    print("le produit des entiers paires est :",p)
    print("le nombres des entiers paires est :",nm)

n=int(input("entrez le 1er entier :"))
m=int(input("entrez le 2éme entier :"))
if(n>m):
   t=m
   m=n
   n=t
somme_produit(n,m)