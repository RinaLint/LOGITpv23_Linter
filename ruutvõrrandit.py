#1
from random import *
from math import *
number=float(input("Sisestage number: "))
if number >0:
    print("Number on positiivne")
    if number%2==0:
       print("Number paarisarv")
    else:
        print("Number pole paaris")
elif number <0:
    print("Number on negatiivne")
else:
    print("Number on null")





#2
from math import *
a,b,c=map(float,input("a,b,c:").split())
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("Kolmnurk")
        if a==b==c:
            print("Võrdkülgne")
        elif a==b or b==c or c==a:
            print("Võrdhaarne")
        else:
            print("Erikülgne")
    else:
        print("Nurgad")
else:
    print("<0")





#3
from math import *
vastus=input("Kas tahad 1-7 numbrist saada päeva nimetus?").capitalize()
if vastus.lower()=="jah":
    try:
        nr=int(input("Päeva number: "))
        if nr==1:
            p="esmaspäev"
        elif nr==2:
            p="teisipäev"
        elif nr==3:
            p="kolmapäev"
        elif nr==4:
            p="neljapäev"
        elif nr==5:
            p="reede"
        elif nr==6:
            p="laupäev"
        elif nr==7:
            p="pühapäev"
        else:
            p="on vaja 1-7"
        print(p)
    except :
        pass
   




#4
from math import *
day=int(input("Sisestage oma sünnipäev:"))
month=int(input("Sisesta sünnikuu:"))
if month<1
    try:
        if (month==3 and day>=21) or (month==4 and day<=19):
             print("Jäär")
        elif (month==4 and day>=20) or (month==5 and day<=20):
             print("Vasikas")
        elif (month==5 and day>=21) or (month==6 and day<=20):
             print("Kaksikud")
        elif (month==6 and day>=21) or (month==7 and day<=22):
             print("Vähk")
        elif (month==7 and day>=23) or (month==8 and day<=22):
             print("Lõvi")
        elif (month==8 and day>=23) or (month==9 and day<=22):
            print("Neitsi")
        elif (month==9 and day>=23) or (month==10 and day<=22):
             print("Kaalud")
        elif (month==10 and day>=23) or (month==11 and day<=21):
             print("Skorpion")
        elif (month==11 and day>=22) or (month==12 and day<=21):
             print("Ambur")
        elif (month==12 and day>=22) or (month==1 and day<=19):
             print("Kaljukits")
        elif(month==1 and day>=20) or (month==2 and day<=18):
             print("Veevalaja")
        elif (month==2 and day>=19) or (month==3 and day<=20):
             print("Kalad")
        else:
             print("Sinu sodiaagimärk")
    except :
      print("Viga")
else:
   print("Arv on negatiivne!")





#5
vastus=float(input("Введите число: "))
try:
    if vastus.isdigit():
        number=int(vastus)






#6
from math import *
vastus=input("Kas lahendame ruutvõrrand?").lower()
if vastus=="jah":
    print("Ruutvõrrandi lahendamine:")
    try:
        #a,b,c=map(float,input("a,b,c:")).splite(",")
        a=float(input("a: "))
        b=float(input("b: "))
        c=float(input("c: "))
        D=b**2-4*a*c
        if D>0:
            x1=(-b+sqrt(D))/2*a
            x2=(-b-sqrt(D))/2*a
            print("2 lahendust 1:{0:.2f},2:{1:.2f} ".format(x1,x2))
        elif D==0:
            x1=(-b)/2*a
            print("1 lahendust {0:.2f} ".format(x1))
        else:
            print("Lahendused puuduvad")
    except :
        print("Viga andetüübiga")
else:
    print("Head aega!")
