print("entrez le nombre de photocopies effectuées :")
n=int(input())
if(n>0):
 if(n<=10):
    p=n*0.5
 if(n<=30):
  p=10*0.5+(n-10)*0.30
  print("le prix a payer pour les 10 premiéres photocopies est 5 dh ")
  print(f"le prix a payer pour les {n-10} suivants est  {(n-10)*0.30} dh ")
 else:
  p=10*0.5+20*0.30+(n-30)*0.25
  print("le prix a payer pour les 10 premiéres photocopies est 5 dh ")
  print(f"le prix a payer pour les 20 suivants est 6 dh ")
  print(f"le prix a payer pour les {(n-30)*0.25}  dh")
print(f"le prix total a payer pour les {n} photocipies est {p}")