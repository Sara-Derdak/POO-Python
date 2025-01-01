L=[1,2,-3,4,6,-9]
s=0
min=L[0]
max=L[0]
for x in L:
    s=s+x
    if(min>x):
        min=x
    if(max<x):
        max=x
print("la somme est ",s)
print("la moyenne est ",s/len(L))
print("le max est ",max)
print("le min est ",min)
