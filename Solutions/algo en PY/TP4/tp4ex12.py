print("entrez le premiére entier")
a=int(input())
print("entrez le deuxiéme entier")
b=int(input())
print("entrez l'opérateur qui vous l'utilisez")
c=input()
if(c=="+"):
    print("la somme de deux entier est",a+b)
elif(c=="-"):
    print("la soustraction de deux entier est ",a-b)
elif(c=="*"):
    print("la multiplication de deux entier est ",a*b)
else:
     if(b==0):
         print("la division sur 0 est impossible")
     else:
         print("la division de deux entier est ",a/b)
print("au revoire")