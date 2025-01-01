#1-la longueur d-une chaine sans utiliser la méthode len()
#def taille(chaine):
#    N=0
#    for s in chaine :
#       N=N+1
#        #N+=1
#    return N
#chaine="sara"
#print(taille(chaine))


#2-Le premier mots parmi un text
#def first_word(text):
#    c=text.split()
#    caze1=c[0]
#    return caze1
#text="Longueur dune chaine sans utiliser la méthode len"
#mot=first_word(text)
#print(mot)


#3-Tout les commencant par la lettre a
#def carac_1(T):
#    L=[]
#    c=T.split()
#    for x in c :
#       if(x[0]=="a" or x[0]=="A" ):
            #print(x)"procédure"
#           L.append(x)
#   return L
#T=input("donnez votre text : ")
#print(carac_1(T))


#4-Commencant par majuscule
#def Majuscul(T):
#    L=[]
#    c=T.split()
#    for x in c :
#       if(x[0].isupper()):
#        L.append(x)
#    return L
#T="Écrivez un programme Qui supprime tous les éléments en Double d'une Liste donnée, en conservant l'ordre initial des éléments. "
#print(Majuscul(T))


#5-les étoilles entre les lettres
#def etoiles(chaine):
#    newchaine=""
#    c=chaine.split()
#   for c in chaine :
#        newchaine=newchaine + c + "*"
#        l=len(newchaine)
#         R=newchaine[0;l-1]*********
#    return  R
#T=input("donnez votre mot : ")
#print(etoiles(T))


#les mots
#def listwords(chaine):
#    r=chaine.split()
#    return r  
#T=input("donnez votre text : ")
#print(listwords(T))