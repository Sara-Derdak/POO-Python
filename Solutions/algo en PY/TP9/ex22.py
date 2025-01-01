def occurrences(L,b):
    C=0  
    for i in range (len(L)):
        if b==L[i] :
            C=C+1
    return C
            

L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
b=int(input("donner une valeur : "))
print(f"l'élément {b} se rep {occurrences(L,b)}")