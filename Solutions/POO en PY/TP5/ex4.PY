class Etudiant :
    def __init__(self,n,a,m):
        self.__nom=n
        self.set_age(a)
        self.set_moyenne(m)
        
    def get_nom(self):
        return self.__nom
    
    def set_nom(self,n):
        self.__nom=n
        
    def get_age(self):
        return self.__age
    
    def set_age(self,a):
        if isinstance(a,int) and a>=18 and a<=26 :
            self.__age=a
        else:
            raise Exception("age must be between 18 and 26")
        
    def get_moyenne(self):
        return self.__moyenne
    
    def set_moyenne(self,m):
        if isinstance(m,int) or isinstance(m,float) and  m>=0 and m<=20 :
            self.__moyenne=m
        else:
            raise Exception("moyenne must be between 0 and 20")
    
    def __str__(self):
        return f"le nom :{self.__nom} l age {self.__age} le moyenne :{self.__moyenne}"
        
        
        
e=Etudiant("ali",18,15.5)
print(e)
print(e.get_age())
e.set_age(20)
print(e)