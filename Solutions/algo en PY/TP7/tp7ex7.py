def table_de_multiplication(n,m):
    for i in range(n,m+1):
        print("le tableau de multiplicatin de ",i)
        for j in range(1,11):
            p=i*n
            print(n,"*",i,"=",p)

n=int(input("entrez le 1er entier :"))
m=int(input("entrez le 2éme entier :"))
if(n>m):
   t=m
   m=n
   n=t
table_de_multiplication(n,m)        