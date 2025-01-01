

from abc import ABC,abstractmethod
from datetime import date

class Employe(ABC):
    def __init__(self,m,n,p,d):
        self.__nom=n
        self.__matricule=m
        self.__prenom=p
        self.__datenaissance=d
        
    def get_nom(self):
        return self.__nom
    def set_nom(self,n):
        self.__nom=n
        
    def get_prenom(self):
        return self.__prenom
    def set_prenom(self,p):
        self.__prenom=p
        
    def get_matricule(self):
        return self.__matricule
    def set_matricule(self,m):
        self.__matricule=m
        
        
    def get_datenaissance(self):
        return self.__datenaissance
    def set_datenaissance(self,d):
        if d > 0:
         self.__datenaissance=d
        else : 
            print("la date invalide")
            
            
    def __str__(self):
        return f"Nom complet : {self.__nom,self.__prenom} , Le matricule : {self.__matricule}"
    
    
    @abstractmethod
    def getsalaire(self):
        pass
    
    
class Ouvrier(Employe):
    __SMIG=3000
    def __init__(self, m, n, p, d , a):
        super().__init__(m, n, p, d)
        self.__dateentre=a
        
    def get_dateentre(self):
        return self.__dateentre
    def set_dateentre(self,d):
        if d > 0:
         self.__dateentre=d
        else : 
            print("la date invalide")
        
        
    @staticmethod
    def get_SMIG():
        return Ouvrier.__SMIG
    def set_SMIG(V):
       Ouvrier.__SMIG=V
       
       
    def getsalaire(self):
        a=int((date.today- self.__dateentre).days)/365.25)
        s=Ouvrier.__SMIG + a * 100
        if s < Ouvrier.__SMIG * 2 :
         return s
        else :
         return Ouvrier.__SMIG * 2 
    
    def __str__(self):
       return super().__str__()+f" , mon profil est ouvrier "
   
   
class Cadre(Employe):
    def __init__(self, m, n, p, d, i):
       super().__init__(m, n, p, d)
       self.set_indice(i)
           
    def get_indice(self):
        return self.__indice
    def set_indice(self,i):
        if (i==1 or i==2 or i==3 or i==4 ):
          self.__indice=i
        else:
            print("Indice invalide")
            
    def getsalaire(self):
      if self.__indice==1 :
        return 130000/12
    
      elif self.__indice==2 :
        return 150000/12
    
      elif self.__indice==3 :
        return 170000/12
    
      elif self.__indice==4 :
        return 200000/12
    
            
    def __str__(self):
       return super().__str__()+f" , mon profil est cadre "
   
   
class Patron(Employe):
    __pourcentage_aff=None
    def __init__(self, m, n, p, d ,c):
       super().__init__(m, n, p, d)
       self.__chiff_aff=c
       
    @staticmethod
    def definir_pourcentage_aff (p):
        Patron.__pourcentage_aff = p
    def get_taux_interet ():
        return Patron.__pourcentage_aff 
    
    def get_chiff_aff(self):
        return self.__chiff_aff
    def set_chiff_aff(self,c):
        self.__chiff_aff=c
        
    def getsalaire(self):
        return self.__chiff_aff*Patron.__pourcentage_aff/100
    
    def __str__(self):
       return super().__str__()+f" , mon profif est patron "
        
    
    
    
o=Ouvrier(1,"nom1","prenom1","2000-01-01",date(2020,12,30))
print("Mon salaire mensuel",o.getsalaire(),"dh")
print(o) 

# c=Cadre(2,"nom2","prenom2","1998-02-02",1)
# print(c)
# print("Mon salaire mensuel",c.getsalaire(),"dh")

# p=Patron(3,"nom3","prenom3","1995-03-03",5)
# print(p)
# print("Mon salaire annuel",p.getsalaire(),"dh")






# from datetime import datetime

# now = datetime.now()
# print(now)

# from datetime import datetime

# date_string = "2023-12-26"
# formatted_date = datetime.strptime(date_string, "%Y-%m-%d")
# print(formatted_date)

# from datetime import datetime

# now = datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)