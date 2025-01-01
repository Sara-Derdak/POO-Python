M=0
N=0
P=0
for i in range(1,11):
    print("entrer l'entier")
    e=int(input())
    if(e==0):
        M=M+1
    elif(e<0):
        N=N+1
    else:
        P=P+1
print("Les nombres nules",M)
print("Les nombres négatifs",N)
print("Les nombres positifs",P)
