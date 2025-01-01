#while True:
    #print(" donner une note entre 0 et 20 ")
    #n=float(input())
    #if(n>=0 and n<=20):
      #  break
    #else:
     #   print("votre note est invalide")
#print("la note est :",n)


print(" donner une note entre 0 et 20 ")
n=float(input())
while(n<0 or n>20):
    print("votre note est invalide")
    print(" donner une note entre 0 et 20 ")
    n=float(input())
print("la note est :",n)