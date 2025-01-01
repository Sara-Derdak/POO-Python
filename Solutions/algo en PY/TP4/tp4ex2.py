
R=0.01
print("entrz le prix unutaire")
pu=float(input())
print("entrez la quantité :")
q=float(input())
pp=pu*q
if(pp>5000):
    pp=pp-pp*R
print("le prix a payer est :",pp)
