mydic={"device":"laptop","constructeur":"acer","ram":"8G","processeur":"Intel core i5","stockage":"500G"}

mydic["stockage"]="750G"

print("*************************")

for i in mydic :
    print(i)

print("**************************")


for i in mydic.values():
    print(i)

print("**************************")

for i,j in mydic.items():
    print("cle : ",i," / valeur : ",j)

# for i,j in mydic.items():
#     print("cle : ",i)
#     print("value : ",j)
#     print(i,j)
#     print("****")




mydic["Systeme d'exploittion"]="Windows 10"

print(mydic)