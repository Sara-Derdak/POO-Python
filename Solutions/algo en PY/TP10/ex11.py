def Moyenne(T):
    s=0
    for x in T:
        s=s+len(x)
    N=s/len(T)       
    return N
T=['sara','derdak','dev']
print("La longueur moyenne des chaines : ",Moyenne(T))