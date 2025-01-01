
c=5000
r=0.22
print("entrez le salaire par heure")
sh=float(input())
print("entrez le nombre d'heure travaillées")
nh=float(input())
s=sh*nh
t=s*r
if(t>c):
    sm=s-c
else:
    sm=s-t
print("le salsire mensuel est :",sm,"dh")