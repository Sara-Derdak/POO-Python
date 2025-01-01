import math
print("entrez la valeur de a")
a=int(input())
print(" entrez la valeur de b")
b=int(input())
print(" entrez la valeur de c")
c=int(input())
if(a==0):
    print("cette équation n'est une éqution de deuxiéme degré")
t=b*b-4*a*c
if(t>0):
    x1=-b-math.sqrt(t)/2*a
    x2=-b+math.sqrt(t)/2*a
    print("l'éqution admet deux solution x1=",x1," et x2=",x2)
elif(t==0):
    x=-b/2*a
    print("l'équation admet aucune solution x=",x)
else:
    print("l'équation n'admet aucune solution dans l'ensemble R")
print("Au revoire")