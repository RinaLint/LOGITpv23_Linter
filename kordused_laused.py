from random import *
from datetime import *

#3 l
k=0
while True:
    k+=1
    a=randint(1,50)
    b=randint(1,50)
    p=0
    while p!=3:
        p+=1
        v=int(input("Millega võrdub {0}+{1}".format(a,b)))
        if v==a+b:
            print("Tubli!")
            break
        else:
            print("Mõtle veel!")
    print("{0}+{1}={2}".format(a,b,a+b))

    if k==5:break





#2 l
summa=0
for i in range(10):
    arv=float(input("Sisesta arv: "))
    summa+=arv
print(summa)

summa=0
i=0
while True:
    i+=1
    arv=float(input("Sisesta arv: "))
    summa+=arv
    if i==10: break
print(summa)


#1
nimi=input("Mis on sinu nimi?").capitalize()
mitu=int(input("Mitu korda tervitada?"))
for i in range(1, mitu+1):
    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")




#Praktiline töö "Tsükkel"
#0
while True:
    v=input("Kas sul on trenn?").lower()
    if v=="jah": break

print("2. varindt -while tingimusega-")
v=""
while v!="jah":
    v=input("Kas sul on trenn?").lower()




paevad=["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]
trennid=["trenn on olemas", "trenn ei ole olemas", "trenn on olemas", "trenn ei ole olemas", "trenn on olemas", "trenn on olemas", "trenn ei ole olemas"]
for i in range(7):
    print(paevad[i]+"-"+trennid[i])





#3 Komm
while True:
    v=input("Tahan komme!").lower()
    if v=="komm": break

print("2. varindt -while tingimusega-")
v=""
while v!="komm":
    v=input("Tahan komme!").lower()




#2 Nädala päevad
paevad=["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]
tunnid=["8 tundi", "9 tundi", "8 tundi", "5 tundi", "6 tundi", "tunde pole", "tunde pole"]
for i in range(7):
    print(paevad[i]+"-"+tunnid[i])





#1 Poes korduslausega
arve_nr=datetime.now() #date.today()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
toodet=["Piim", "Leib", "Komm"] #index 0-1-2
for i in range(3): #i=0, i=1, i=2
    toode1=toodet[i]
    hind=randint(50,150)/100
    v=input("Toode:"+toode1+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu?"))
        tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
        summa+=mitu*hind

tsekk+="Kokku maksta: "+str(summa)
print(tsekk)