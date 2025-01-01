def maximum(a,b,c):
    max=a
    if(b>max):
        max=b
    if(c>max):
        max=c
    return max
a=float(input("entrez la 1er valeure :"))
b=float(input("entrez la 2éme valeure :"))
c=float(input("entrez la 3éme valeure :"))
m=maximum(a,b,c)
print("le maximum est :",m)