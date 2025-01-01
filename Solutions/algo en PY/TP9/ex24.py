def Majuscul1(T):  
    L=[]
    for x in T :
       if(x[0].isupper()):
        L.append(x)
    return L


L=['Bonjour','dev','Algo']
print("les mots commençant par une majuscule dans le texte sont : ",Majuscul1(L))