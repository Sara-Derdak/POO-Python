while True:
    print("choisissez une opération ")
    print("1-Addition")
    print("2-Sustraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Quitter")
    n=int(input("donner votre choix :"))
    if(n==5):
        print("ok, au revoire !")
        break
    elif(n==1 or n==2 or n==3 or n==4):
        a=float(input("entrez le premiére nombre"))
        b=float(input("entrez le deuxiéme nombre"))
        if(n==1):
            r=a+b
        elif(n==2):
            r=a-b
        elif(n==3):
            r=a*b
        elif(n==4):
            while(b==0):
                print ("division par 0 est impossible")
                b=float(input("entrez le nombre"))
            r=a/b
        print("le résultat est : ",r)
    else:
        print("opération invalide")