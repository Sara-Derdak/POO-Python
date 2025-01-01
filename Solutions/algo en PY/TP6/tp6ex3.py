def prix(q,pu,tva):
    pht=q*pu
    pt=pht+(pht*(tva/100))
    return pt
q=int(input("entrez la quantitée :"))
pu=float(input("entrez le prix unitaire :"))
tva=float(input("entrez le taux de TVA :"))
PT=prix(q,pu,tva)
print("le prix total est :",PT)