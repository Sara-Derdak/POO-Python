print("entrez l'heure")

h=int(input())

print("entrez les minutes")
m=int(input())
print("entrez les secondes")
s=int(input())
if(h<0 or h>24 or m<0 or m>59 or s<0 or s>59):
    print("ereur")
else:
    s=s+1
    if(s>59):
        s=0
        m=m+1
        if(m>59):
            m=0
            h=h+1
            if(h>23):
                h=0
    print(f"l'heure aprés une seconde est {h} : {m} : {s}")