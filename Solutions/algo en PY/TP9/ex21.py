# def repetition(L):
#     R=[]
#     for x in L :
#         if x not in R :
#             R.append(x)
#     return R
def Dupli(L):
    L2=[]
    L3=[]
    for x in L:
        if x not in L2 :
            L2.append(x)
        else :
            L3.append(x)
    return L3

L=[]
print("entrez la longueur de la liste")
N=int(input())
for i in range(0,N):
    print("entrez la valeur ",i+1)
    a=int(input())
    L.append(a)
print(L)
# print(repetition(L))
print(Dupli(L))