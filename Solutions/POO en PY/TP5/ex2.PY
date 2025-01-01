# L=[]
# try :
#     while True :
#         N=int(input("donner la longueur de la liste"))
#         if N>0 :
#             break
        
# except ValueError as e :
#     print("erreur")
    
    
# try:
#  for i in range(N):
#     print("donner la valeur ",i+1)
#     a=int(input())
#     L.append(a)
# except ValueError as e:
#     print(e)
    
# except :
#     print("error !!!!")
    
# try:
#     i=int(input("donner votre index : "))
#     print(L[i])
# except IndexError as e:
#     print(e)
    
# except ValueError as e:
#     print(e)
    
# except :
#     print("error !!!!")

try:
    L=[1,3,59,5]
    print(L[7])
except IndexError as e:
    print(e)
except:
    print("error !!!!")