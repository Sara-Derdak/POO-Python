L=[1,2,2,3,4,4,5,6]
L2=[]
for i in L:
    if i not in L2 :
        L2.append(i)
L=L2
print(L)
