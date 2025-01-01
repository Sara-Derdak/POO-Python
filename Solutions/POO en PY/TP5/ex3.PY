try:
    print("donner une chainne")
    a=input()

    n=int(input("donner le premier index : "))
    m=int(input("donner le deuxieme index : "))
    if n>m :
        t=n
        n=m
        m=t
    c=""
    for i in range(n,m+1):
        c=c+a[i]
    print(c)
except Exception as a:
    print(a)

# except IndexError as a:
#     print(a)
# except:
#     print("error!")