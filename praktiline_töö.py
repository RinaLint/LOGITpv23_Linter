from random import *
from detetime import *

#8 Poes
arve_nr=datetime.now() #date.today()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
toode1="Piim"
hind=randint(50,150)/100
v=input("Toode:"+toode1+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
print(tsekk)
toode2="Saia"
hind=randint(90,300)/100
v=input("Toode:"+toode2+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode2+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
print(tsekk)
toode3="Leib"
hind=randint(600,1500)/100
v=input("Toode:"+toode3+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mitu?"))
    tsekk+=toode3+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)


#7 Inimese pikkus ja sugu
sugu=input("Kas sa oled mees või naine?").lower()
if sugu=="naine" or sugu=="n":
    l1=155
    l2=270
    l3=255
elif sugu=="mees" or sugu=="m":
    l1=160
    l2=180
    l3=255
else:
    l1=0
    print("Viga")
if l1!=0: #l1==155 or l1=160
    print("Viga")
    try:
         pikkus=int(input("Sisesta oma pikkus: "))
         if pikkus>29 and pikkus<l1: #100
            vastus="lühike"
         elif pikkus>=l1 and pikkus<l2: #165
            vastus="keskmine"
         elif pikkus>=l2 and pikkus<=l3: #200
            vastus="pikk"
         else:                         #-10, 300
            vastus="tundmatu"
         print("Sinu pikkus on {0}".format(vastus))
    except :
         print("Vale andmete formaat!")





#6 inimese pikkus
try:
    pikkus=int(input("Sisesta oma pikkus: "))
    if pikkus>29 and pikkus<155: #100
        vastus="lühike"
    elif pikkus>=155 and pikkus<170: #165
        vastus="keskmine"
    elif pikkus>=170 and pikkus<=255: #200
        vastus="pikk"
    else:                         #-10, 300
        vastus="tundmatu"
    print("Sinu pikkus on {0}".format(vastus))
except :
    print("Vale andmete formaat!")





#5
try:
    t=float(input("Mis on ruumi temperatuur?"))
    if t>18:
       print(str(t))
    else:
        print("See on külm")
except:
    print("Viga")





#4
try:
    hind=float(input("Hind: "))
    if hind>=700:
        hind*=0.7
        print(hind)
    print(hind)
except :
    print("Viga")



#3
try:
    pikkus=float(input("Pikkus:"))
    try:
        laius=float(input("Laius:"))
        S=pikkus*laius
        print("Pindala võrdub", S)
        soov=input("Kas tahad remondi teha?").lower() #Jah, #jah, #JAH -> jah upper()->JAH
        if soov=="jah" or soov=="да":
            try:
                hind=float(input("Ruutmeetri hind: "))
                summa=hind*S
                print("Remondi summa on", summa)
            except:
                print("Viga")
        else:
            print("Head aega")
    except :
        print("Viga")
except :
    print("Viga")







#2
eesnimi1=input("Mis on 1. nimi?").capitalize() # "Karina" "Egor"
eesnimi2=input("Mis on 2. nimi?").capitalize()
if (eesnimi1=="Karina" and eesnimi2=="Egor") or (eesnimi1=="Egor" and eesnimi2=="Karina"):
    print("Need on pinginaabrid")
else:
    print("Rühmakaaslased")

if (eesnimi1!=eesnimi2) and (eesnimi1 and eesnimi2 in ["Karina", "Egor"]):
    print("Need on pinginaabrid")
else:
    print("Rühmakaaslased")






#1
eesnimi=input("Mis on sinu nimi?").capitalize() #Juku
if eesnimi=="Juku":
    try:    
        vanus=int(input("Kui vana sa oled?"))
        print("Jukule ostame ", end="")
        if 0<vanus<6:
            print("tasuta pilet")
        elif 6<=vanus<=14:
            print("lastepilet")
        elif 14<vanus<=65:
            print("täispilet")
        elif 65<vanus<=100:
            print("sooduspilet")
        else:
            print("Mitte midagi. Viga andmetega!")
    except:
        print("Int andmetüüp on vaja kasutada!")
else:
    print("Mine ise kinno!")