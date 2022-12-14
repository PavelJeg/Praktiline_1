from ast import excepthandler
from importlib.resources import Package
from math import *
from stringprep import c22_specials, c6_set
from tkinter import Pack
from tkinter.tix import InputOnly # * -kõik funktsioonid moodulist
from random import *
from xml.dom.minidom import Identified
#import math       math.funktsioon()
#12/12/22
#1.
print("Puu läbimõõdu arvutamine")
#Kirjuta programm,mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
try:
    C=float(input("Anna ümbermõõt: "))
    if C>0:
        d=round(C/pi,2)
        print(f"Puu läbimõõt = {d}")
    else:
          print("C peab olema suurem kui 0")
except:
    print("Andmetüüp on vale")



print("Ristkülikukujulise maatüki diagonaal pikk")
try:
    N=float(input("Siseta N: "))
    M=float(input("Siseta M: "))
    if M>0 and N>0:
        d=round(sqrt(N**2+M**2),2)
        print("Ristkülikukujulise maatüki diagonaal pikk ",round(d,2))
except:
    print("N jf M olema suurem kui 0")


try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    if aeg>0 and teepikkus>0:
        kiirus = teepikkus / aeg
        print("Sinu kiirus oli " + str(kiirus) + " km/h")

except:
    print("M ja N vaja sisetafda float formaadis")

print("Aritmeetiline keskmine")
A1=int(input("Esimine arv: "))
A2=int(input("Teine arv:   "))
A3=int(input("Kolmas arv:  "))
A4=int(input("Neljas arv:   "))
A5=int(input("Viies arv:   if"))
if A1>0 and A2>0 and A3>0 and A4>0 and A5>0:
    K=(A1+A2+A3+A4+A5)/5
else:
    print("aeg ja teepikkus vaja sisetada float formaadis ")
    print(f"Kesknime on {k}")




print("      @..@")
print("     (----)")
print("    ( \__/ )")
print('    ^^ "" ^^')



a=randint(0,100)
b=randint(0,100) 
c=randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
P=a+b+c
print(f"Ümbermõõt on {P}")




P=randint(1,6)
summa=(12.9*1.1)/P
print(f"{P}-st, Igaüks maksab {summa}")



print("Kütusekulu arvutamine")
l=float(input("Kütuse liitride kogus:"))
km=float(input("Läbitud kilomeetrid"))
kulu=(l/km)*100
print(f"Kütusekulu {kulu}")




print("Rulluisutajad")
M=int(input("Minutid:"))
M=M/60
tee=M*29.9
print(f"Jõuab {tee} km")




print("Ajateisendus")
m=int(input("Sisesta aja minutites")) #1h=60min
H=M//60 #h
M=M%60 #min
print(f"{H}:{M}")





print("Ema mis hined sa koolis said?")
a=input("Siseta: ")
print(a.isalpha(), a.isdigit())
if a.isdigit() and int(a)>0 and int(a)<=5:
    a=int(a)
    if a==5:
        pass
    elif a==4:
        pass
    elif a==3:
        pass
    elif a==2 or a==1:
            pass
else:
    print("Sa valesti vastas")

