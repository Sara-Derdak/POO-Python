def parf(i):
    s=0
    for j in range(1,i):
        if(i%j==0):
            s=s+j
    if(s==i):
        p=True
    else:
        p=False
    return p

def sublimes(m,n):
    for i in range(m,n+1):
        sd=0
        nd=0
        for j in range(1,i+1):
            if(i%j==0):
                nd=nd+1
                sd=sd+j
        if ((parf(nd)==True) and (parf(sd)==True)):
            print(i)


print("entrez les entiers ")
m=int(input())
n=int(input())
print("les nombres sont")
sublimes(m,n)
