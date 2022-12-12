from importlib.resources import Package
from math import *
from stringprep import c22_specials, c6_set
from tkinter import Pack
from tkinter.tix import InputOnly # * -kõik funktsioonid moodulist
from random import *
#import math       math.funktsioon()
#12/12/22
#1.
print("Puu läbimõõdu arvutamine")
#Kirjuta programm,mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
C=float(input("Anna ümbermõõt: "))
d=round(C/pi,2)
print(f"Puu läbimõõt = {d}")



print("Ristkülikukujulise maatüki diagonaal pikk")
N=float(input("Siseta N: "))
M=float(input("Siseta M: "))
d=round(sqrt(N**2+M**2),2)
print("Ristkülikukujulise maatüki diagonaal pikk ",round(d,2))


aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")



print("Aritmeetiline keskmine")
A1=int(input("Esimine arv: "))
A2=int(input("Teine arv:   "))
A3=int(input("Kolmas arv:  "))
A4=int(input("Neljas arv:   "))
A5=int(input("Viies arv:   "))
K=(A1+A2+A3+A4+A5)/5
print(f"Kesknime on {K}")




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


