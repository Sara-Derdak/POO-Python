def premiers_fct(n):
    s=0
    for i in range(1,n+1):
        if(n%i==0):
            s=s+i
    if(s==2):
        p=True
    else:
        p=False
    return p

def premier(m,n):
    for i in range(m,n+1):
        if(premiers_fct(i)==True):
            print(i)

m=int(input("entrez le 1er entier :"))
n=int(input("entrez le 2éme entier :"))
if(n>m):
   t=m
   m=n
   n=t
premier(m,n)