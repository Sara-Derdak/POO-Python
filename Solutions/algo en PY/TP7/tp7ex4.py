def equation (a,b):
    if(a!=0):
        print(-b/a)
    elif(b==0):
        print("l'ensemble R")
    else:
        print("l'enesmble vide")

print("entrez les nombres nécéssaires")
a=float(input())
b=float(input())
equation (a,b)