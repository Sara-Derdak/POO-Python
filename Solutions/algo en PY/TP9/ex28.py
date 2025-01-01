def sup_entier(L):
    T=[]
    for x in L :
        if  not isinstance(x,int):
            T.append(x)
    L=T.copy()
    return L




L=[1,3,4,4.5,34,5,6.4,6,87,9.8,7]
print(L)
print("la liste modifier est : ",sup_entier(L))