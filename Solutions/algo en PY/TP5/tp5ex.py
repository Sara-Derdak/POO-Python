#while True:
   # print("entrez un nombre strictement positif")
   # n=int(input())
    #if(n>0):
     #   break
   # else:
    #    print("le nombre invalide")
#print(n)


print("entrez un nombre strictement positif")
n=int(input())
while(n<=0):
    print("le nombre invalide")
    print("entrez un nombre strictement positif")
    n=int(input())
print(n)