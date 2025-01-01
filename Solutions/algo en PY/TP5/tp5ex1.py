print("entrez le nombre des notes")
nn=int(input())
t=0
for i in range(1,nn+1):
    print("entrez la note ")
    n=float(input())
    t=t+n
print("la moyenne est :",t/nn)
