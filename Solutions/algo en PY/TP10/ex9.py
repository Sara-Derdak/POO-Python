def s_doublons(T):
    D=[]
    for x in T :
        if x not in D :
           D.append(x)
    return D
L=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=input()
    L.append(a)
print(s_doublons(L))
