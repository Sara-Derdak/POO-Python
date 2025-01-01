while True:
  print("1-convertir de DH vers Euro")
  print("2-convertir de Euro vers DH ")
  print("3-Quitter")

  print("Quel est votre choix :")
  c=int(input())
  if(c==1 or c==2 or c==3):
      if(c==1):
        print("entrey le montant en dh")
        m=float(input())
        print("le montant en euro est : ",m/10)
        
      elif(c==2):
        print("entrey le montant en euro")
        m=float(input())
        print("le montant en dh est :",m*10)
        
      if(c==3):
        break
print("merci au revoire ")