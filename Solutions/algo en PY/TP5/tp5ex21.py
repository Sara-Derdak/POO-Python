while True:
    print("entrez votre entier")
    e=int(input())
    for i in range(1,11):
        p=i*e
        print(i,"x",e,"=",p)
    while True:
        print("voulez vous ajouter un autre entier (o/n) :")
        c=input()
        if(c=="o" or c=="O"):
            break