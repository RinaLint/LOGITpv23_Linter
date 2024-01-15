#iseseisev töö. valik laused

from math import *
a,b,c=map(float,input("a,b,c:")).splite(" ")
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("Kolmnurk")
        if a==b==c:
            print("võrdkülgne")
        elif a==b or b==c or a==c:
            print("erikülgne")
    else:
        print("Nurgad")
else:
    print("<0")

#6
from math import *
vastus=input("Kas lahendame ruutvõrrand?").lower()
if vastus=="jah":
    print("Ruutvõrrandi lahendamine:")
    try:
        #a,b,c=map(float,input("a,b,c:")).split(",")
        a=float(input("a: "))
        b=float(input("b: "))
        c=float(input("c: "))
        D=b**2-4*a*c
        if D>0:
            x1=(-b+sqrt(D))/2*a
            x2=(-b+sqrt(D))/2*a
            print("2 lahedust 1:{0:.2f},2:{1:.2f} ".format(x1, x2))
        elif D==0:
            x1=(-b)/2*a
            print("1 lahendus: {0:.2f} ".format(x1))
        else:
            print("Lahendused puuduvad")
    except :
        print("Viga  andmetüübiga")
else:
    print("Head aega!")


#5


#4


#3



#2
from math import *
a,b,c=map(float,input("a,b,c:")).splite(",")
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("Kolmnurk")
        if a==b==c:
            print("võrdkülgne")
        elif a==b or b==c or a==c:
            print("erikülgne")
    else:
        print("Nurgad")
else:
    print("<0")




from random import *
from math import *
#1
number=float(input("Sisestage number: "))
if number>0:
    print("Arv on positiivne")
    if number%2==0:
        print("Number paarisarv")
    else:
        print("Number pole paaris")
elif number<0:
    print("arv on negatiivne")
else:
    print("arv on null")