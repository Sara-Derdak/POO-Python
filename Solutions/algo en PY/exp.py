from sarab import somme_produit

n=int(input("entrez le 1er entier :"))
m=int(input("entrez le 2éme entier :"))
if(n>m):
   t=m
   m=n
   n=t
somme_produit(n,m)

