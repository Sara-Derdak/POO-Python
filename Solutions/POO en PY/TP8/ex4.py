def occurence(L):
    d={}
    for i in L :
        d[i]=L.count(i)
    return d


L=[1,3,2,1,4,1,2,1]
print(occurence(L))