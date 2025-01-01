def carac_1(T,l):
    L=[]
    for x in T :
       if(x[0]==l):
        L.append(x)
    return L
           

T=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=input()
    T.append(a)
l=input("donnez la lettre qui vous voulez : ")
print("les mots qui commence par la lettre ",l,"sont",carac_1(T,l))


