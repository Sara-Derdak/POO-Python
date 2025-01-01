def  palindrome(L):
    LL=[]
    for x in L :
        if x == x[::-1]:
            LL.append(x)
    return LL
  

L=[]
print("entre le nombres qui vous voulez")
n=int(input())
for i in range(0,n):
    print("entrez la valeur ",i+1)
    a=input()
    L.append(a)
print("les chaines palindromes sont : ",palindrome(L))