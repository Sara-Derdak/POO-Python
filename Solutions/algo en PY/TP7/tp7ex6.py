def table_de_multip(n):
    for i in range(1,11):
        p=i*n
        print(n,"*",i,"=",p)

print("entrez votre entier :")
n=int(input())
table_de_multip(n)