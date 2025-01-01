print("entrez la température d'eau")

T=float(input())
if(T>=100):
    print("l'état d'eau est gaz")
elif(T>=0):
    print("l'état d'eau est liquide")
else:
    print("l'état d'eau est solide")