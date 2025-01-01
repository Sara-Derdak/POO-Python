L=[]
N=int(input("donner la long : "))
for i in range(N):
    c=input(f"donner la chaine N:{i+1}  :")
    L.append(c)
for x in L :
    print(f"la long de la chaine suivantes # {x} # est {len(x)} ")