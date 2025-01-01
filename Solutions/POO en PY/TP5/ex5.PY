class InvalideCINException(Exception):
    pass
class InvalideGradeException(Exception):
    pass

class Employe :
    def __init__(self,c,n,p,g):
        self.__CIN=c
        self.__nom=n
        self.__prenom=p
        self.garde=g
    
        
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n  
        
        
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,p):
        self.__prenom=p 
        
        
    @property
    def CIN (self):
        return self.__CIN
    @CIN.setter
    def CIN(self,c):
        if len(c)==7 and c[0].isalpha() and c[1:].isdigit() :
            self.__CIN=c
        else:
            raise InvalideCINException ("Le CIN est invalide")
        
        
    @property
    def garde(self):
        return self.__garde
    @garde.setter
    def garde(self,g):
        if (g=="a" or g=="A" or g=="b" or g=="B" or g=="c" or g=="C" or g=="d" or g=="D" ):
           self.__garde=g
        else :
            raise InvalideGradeException ("Le garde invalide")   
        
        
    def __str__(self):
        return f"le nom :{self.__nom}, le prenom :{self.__prenom} , le CIN :{self.__CIN} , le garde : {self.__garde}"
        
        
        
        
        
e=Employe("EE12012","Mohammed","Ali","A")
print(e) 
print(e.CIN)
e.garde="B"
print(e.garde)
        
        
        
        
        
        
        
        
        
    
    # def get_nom(self):
    #     return self.__nom
    # def set_nom(self,n):
    #     self.__nom=n
        
    # def get_cin(self):
    #     return self.__CIN
    # def set_cin(self,c):
    #     if True==True :
    #         self.__CIN=c
    #     else:
    #         raise Exception ("CIN invalide")
        
    # def get_prenom(self):
    #    return self.__prenom
    # def set_prenom(self,p):
    #     self.__prenom=p
        
    # def get_garde(self):
    #     return self.__garde
    # def set_garde(self,g):
    #     if (g=="a" or g=="A" or g=="b" or g=="B" or g=="c" or g=="C" ):
    #        self.__garde=g
    #     else :
    #         raise Exception ("Le garde invalide")
        
