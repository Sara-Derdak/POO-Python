
print("entrez une année")
a=int(input())
if((a%4==0 and a%100!=0)or(a%400==0)):
    print(a,"est une année bissextil")
else:
    print(a,"est une année non bissextil")
