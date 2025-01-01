print("entrez votre nombre")
e=int(input())
if(e<0):
    print("doit entrer un nombre positif")
else:
    for i in range(1,10):
        print(f"{e}×{i}={e*i}")