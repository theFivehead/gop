import time
import itertools
import timeit
import math
import sys
from multiprocessing import Process, cpu_count

#definovani promennych --------------------------------------------------------------------------
soubor_prvocislo_n=""
soubor_prvocislo_u="prvocisla.txt"
testovat_prvociselnost=True
cisla=[]
#prepinace
generovat_prv=False     #prepinac -g
ulozit_do_souboru=False #prepinac -u
nacist_ze_souboru=""    #prepinac -n="cesta ke souboru"

def help():
    print("-g pro generování prvočísel\n-u ulozit_do_souboru\n-n=""cesta ke souboru""\n--help zobrazí tento text")
    sys.exit()

#funkce ktera nacte cisla ze souboru a vráti pole s int
def nacteni_cisel_soubor(nacteni_lokace):
    soubor=open(nacteni_lokace, "r")
    nactena_data=soubor.read().split("\n")
    cisla=[0]
    for potencialni_cislo in nactena_data:
        if potencialni_cislo.isdigit():
            cisla.append(int(potencialni_cislo))
    soubor.close()
    return cisla

def ulozeni_prvocisel_soubor(prvocisla,soubor_cesta="ulozena_prvocisla"):
    soubor=open(soubor_cesta, "w")
    for prvocislo in prvocisla:
        soubor.write(str(prvocislo)+"\n")
    soubor.close()

def atkinovoSito():
    pass

def millerRabin(n):
    a=()
    if n < 2047:
        a = (2,)
    elif n < 1373653:
        a = (2, 3)
    elif n < 9080191:
        a = (31, 73)
    elif n < 25326001:
        a = (2, 3, 5)
    elif n < 3215031751:
        a = (2, 3, 5, 7)
    elif n < 4759123141:
        a = (2, 7, 61)
    elif n < 1122004669633:
        a = (2, 13, 23, 1662803)
    elif n < 2152302898747:
        a = (2, 3, 5, 7, 11)
    elif n < 3474749660383:
        a = (2, 3, 5, 7, 11, 13)
    elif n < 341550071728321:
        a = (2, 3, 5, 7, 11, 13, 17)
    elif n < 3317044064679887385961981:
        a = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
    d=int((n-1)/2)
    for i in range(len(a)):
        p=pow(a[0],d,n)
        if p!=1 and p-n!=-1:
            return False
    return True
def postupneDeleni():
    pass


#nacteni hodnot z prikazove radky --------------------------------------------------------------------------
if len(sys.argv) <= 1:
    print("zadne hodnoty nebyly zadany")
else:
    for i in range(1,len(sys.argv)):
        if sys.argv[i].find("-") != -1:
            if sys.argv[i].find("--help") != -1:
                help()
            if sys.argv[i].find("u") != -1:
                print("prvocisla se ulozi do souboru")
                ulozit_do_souboru=True
            if sys.argv[i].find("g")  != -1:
                print("prvocisla se budou generovat")
                generovat_prv=True
            if sys.argv[i].find("n=")  != -1:
                soubor_prvocislo_n=sys.argv[i][sys.argv[i].find("=")+1:]
                print("prvocisla se nactou ze souboru:"+soubor_prvocislo_n)
        elif sys.argv[i].isdigit():
            cisla.append(int(sys.argv[i]))

if soubor_prvocislo_n != "":
    cisla=nacteni_cisel_soubor(soubor_prvocislo_n)



print(cisla)

