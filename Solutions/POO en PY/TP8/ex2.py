etudians={"etudians_1":13,"etudians_2":17,"etudians_3":9,"etudians_4":15,"etudiants_5":8,"etudiants_6":14,"etudiants_7":16,"etudiants_8":12}

a={}
b={}
for i,j in etudians.items() :
    if j >= 10 :
        a[i]=j
    else:
        b[i]=j
     

print("les etudiants admis : ",a)
print("les etudiants non admis : ",b)
