def Majuscul(T):
    L=[]
    for x in T :
       if(x.isupper()):
        L.append(x)
    return L

print("entrez votre text ")
s=input()
print(Majuscul(s))
