from random import *
from math import *
#4
u=float(input("Ümbermõõt: ")) #L=pi*2*r=pi*d
d=round(u/pi,2)
print("Läbimõõt =",d)








#3
kokku=randint(1,100)
print("Laual peal on",kokku,"kommid. Mitu tahad süüa?")
kommid=int(input())
kokku-=kommid
print("Nüüd  kokku on",kokku)


vanus=18
eesnimi="Jaak"
pikkus=16.5
kas_käib_koolis=True

print("Muutuja vanus=",vanus,"on", type(vanus))
print("Muutuja eesnimi=",eesnimi,"on", type(eesnimi))
print("Muutuja pikkus=",pikkus,"on", type(pikkus))
print("Muutuja kas_käib_koolis=",kas_käib_koolis,"on", type(kas_käib_koolis))

arv1=float(input("Arv1: "))
t=input("Tehe: ")
arv2=float(input("Arv2: "))
vastus=eval(str(arv1)+t+str(arv2))
print(str(arv1)+t+str(arv2)+"="+str(vastus))
print(arv1,t,arv2,"=",vastus,sep="")
print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))


print("Tere maailm!".center(75,"-"))
nimi=input("Mis on sinu nimi? ").capitalize() #python->Python
print("Tere "+nimi+"!")
print("Tere",nimi+"!")
print("Tere {0}!".format(nimi))
vanus=int(input("Kui vana sa oled?"))  #"21"!=21
print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))
print("Muutuja nimi=",nimi,type(nimi))
print("Muutuja vanus=",vanus,type(vanus))