PHTPA=5
PHTPB=2.5
PHTPC=3
PHTPD=10
PHTPE=7
TVA=0.20 #20/100#
print("entrer la quantité achaté de PA")
QPA=float(input())
print("entrer la quantité achaté de PB")
QPB=float(input())
print("entrer la quantité achaté de PC")
QPC=float(input())
print("entrer la quantité achaté de PD")
QPD=float(input())
print("entrer la quantité achaté de PE")
QPE=float(input())
PHTV=(QPA*PHTPA)+(QPB*PHTPB)+(QPC*PHTPC)+(QPD*PHTPD)+(QPE*PHTPE)
print("le prix HT de vente est :",PHTV,"DH")
PTVA=PHTV*TVA
print("La valeur ajouté est :",PTVA,"DH")
PTTCV=PHTV+PTVA
print ("Le prix toutes taxes comprises de cette vente est :",PTTCV, "DH")