def part_fct(i):
    s=0
    for j in range(1,i):
        if(i%j==0):
            s=s+j
    if(s==i):
        p=True
    else:
        p=False
    return p

def parfait(m,n):
    for i in range(m,n+1):
        if(part_fct(i)==True):
            print(i)

m=int(input("entrez le 1er entier :"))
n=int(input("entrez le 2éme entier :"))
if(m>n):
   t=m
   m=n
   n=t
parfait(m,n)