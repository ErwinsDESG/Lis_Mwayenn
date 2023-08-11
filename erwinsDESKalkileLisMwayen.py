liste=[]
er=int(input("Konbyen not wap mete nan lis la? "))
for i in range(er):
    print("Liste[",i+1,"]",end="")
    liste.append(float(input()))
print(liste)
som=0
som=sum(liste)
mwayenn=0
mwayenn=som/er
if mwayenn>=90 :
    print("Moun sa gen yon : A")
elif 80<=mwayenn<90:
    print("Moun sa gen yon : B")
elif 70<=mwayenn<80:
    print("Moun sa gen yon : C")
elif 60<=mwayenn<70:
    print("Moun sa gen yon : D")
else:
    print("Moun sa gen yon : F")
print("Som not li se :",som)
print("Mwayenn li se :",mwayenn)
print(" ")
print("Fen pwogram!")
