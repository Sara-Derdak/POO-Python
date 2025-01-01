def chaine(T):
    d={}
    c=T.split()
    for i in c:
        d[i]=len(i)
    return d
    


T=input("Donner votre texte : ")
print(chaine(T))