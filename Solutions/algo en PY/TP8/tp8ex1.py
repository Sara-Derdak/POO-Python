from numpy import zeros
T=zeros(1000,int)
s=0
print("Donner le nombre de la valeur (max1000):")
n=int(input())
if(n>0 and n<=1000):
    for i in range (n):
        print("donner la valeur",i+1)
        T[i]=int(input())
        s=s+T[i]
    m=s/n
    print("la somme est",s)
    print("la moyenne est",m)
else:
    print("erreur")
    