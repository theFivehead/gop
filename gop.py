import math
import sys
import time
from random import randrange

#definovani promennych --------------------------------------------------------------------------
soubor_prvocislo_n=""
soubor_prvocislo_u="prvocisla.txt"
testovat_prvociselnost=True
cisla=[]       #neoverene prvocisla
prvocisla=[]   #overena prvocisla
cas_Z=0
cas_K=0
algoritmus=("atkinovoSito","millerRabin","postupneDeleni")

#prepinace
cislo_algoritmu=1
generovat_prv=False     #prepinac -g
ulozit_do_souboru=False #prepinac -u
nacist_ze_souboru=""    #prepinac -n="cesta ke souboru"

#otevre soubor pro debugerr
debug = open("udalosti.log","a")
#zapise do logu textovou zpravu
def zapis_debug(text):
    stext=str(text)
    debug.write(time.strftime("%H-%M-%S--%d/%m/%Y")+":"+stext+"\n")
    debug.flush()

 #zobrazi napovedu
def help():
    print("gop.py [cislo algoritmu]  "
          "[prvočíslo nebo -n=""'cesta ke souboru'""]\n"
          "-g pro generování prvočísel\n-u ulozit_do_souboru\n--help zobrazí tento text\n"
          "1 - atkinovoSito\n2 - millerRabin\n3 - postupneDeleni")
    sys.exit()

#funkce ktera nacte cisla ze souboru a vráti pole s int
def nacteni_cisel_soubor(nacteni_lokace):
    zapis_debug("nacitam cisla ze souboru:"+nacteni_lokace)
    try:
        soubor=open(nacteni_lokace, "r")
        nactena_data=soubor.read().split("\n")
        cisla=[0]
        #zjisti jestli se jedna o prirozene cislo
        for potencialni_cislo in nactena_data:
            if potencialni_cislo.isdigit():
                cisla.append(int(potencialni_cislo))
        soubor.close()
        zapis_debug("nactena cisla:"+str(cisla))
        return cisla
    except FileNotFoundError:
        print("zadaly jste neexistující soubor")
        sys.exit()

def ulozeni_prvocisel_soubor(prvocisla,soubor_cesta="ulozena_prvocisla.txt"):
    soubor=open(soubor_cesta, "w")
    for prvocislo in prvocisla:
        soubor.write(str(prvocislo)+"\n")
    soubor.close()
    zapis_debug("ukladam prvocisla:"+str(prvocisla)+"do souboru:"+soubor_cesta)

def atkinovoSito(strop):
    # Vypsání známých prvočísel 2 a 3, pokud to limit dovoluje
    p = []
    if strop<1:
        return p
    elif strop > sys.maxsize:
        print("hodnota prvocisla je vetsi nez je mozna pamet\nzkuste jiny algoritmus\n")
        return p

    if strop > 2:
        p.append(2)
    if strop > 3:
        p.append(3)

    # Inicializace pole pro označení čísel, zda jsou kandidáty na prvočísla
    # Používáme seznam o velikosti limit+1, abychom mohli indexovat až do limit
    try:
        sieve = [False] * (strop + 1)
    except MemoryError:
        print("prvocislo nebylo mozno nacist do pameti")
        return p

    # Sběr pomocí podmínek dle Atkinova algoritmu
    for x in range(1, int(math.sqrt(strop)) + 1):
        for y in range(1, int(math.sqrt(strop)) + 1):
            # Podmínka jedna: n = 4*x*x + y*y, n mod 12 == 1 nebo 5
            n = 4 * x * x + y * y
            if n <= strop and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            # Podmínka dva: n = 3*x*x + y*y, n mod 12 == 7
            n = 3 * x * x + y * y
            if n <= strop and n % 12 == 7:
                sieve[n] = not sieve[n]
            # Podmínka tři: n = 3*x*x - y*y, x > y, n mod 12 == 11
            n = 3 * x * x - y * y
            if x > y and n <= strop and n % 12 == 11:
                sieve[n] = not sieve[n]

    # Zrušení všech násobků čtverců (ty nejsou prvočísla)
    for r in range(5, int(math.sqrt(strop)) + 1):
        if sieve[r]:
            for i in range(r * r, strop + 1, r * r):
                sieve[i] = False

    # Sběr prvočísel z vyznačeného pole
    for a in range(5, strop):
        if sieve[a]:
            p.append(a)
    return p

#jedna se o deterministickou verzi algoritmu
def millerRabin(n):
    if(n<1):
        return False
    #nacte testovaci cisla tzv. svedky
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
    else:#pokud presahne posledni deterministicke cislo prepne se na nahodny
        a=tuple(randrange(2, 5) for _ in range(100))
    d=int((n-1)/2)
    #otestuje zda se jedna o prvocisla
    for i in range(len(a)):
        p=pow(a[i],d,n)
        if p!=1 and p-n!=-1:
            return False
    return True
#pokud cisla i do odmocniny cisla n jsou delitelne nejedna se o prvocislo
def postupneDeleni(n):
    if n<1:
        return False
    hranice=int(math.sqrt(n))+1
    for i in range(2,int(hranice),1):
        if n%i==0:
            return False
    return True

#nacteni hodnot z prikazove radky --------------------------------------------------------------------------

if len(sys.argv) <= 1:#kontrola poctu argumentu
    print("zadne hodnoty nebyly zadany")
    zapis_debug("zadne hodnoty nebyly zadany")
else:
    if sys.argv[1].isdigit():
        cislo_algoritmu=int(sys.argv[1])
        if cislo_algoritmu not in range(1,4):#pokud je algoritmus mimo rozsah <1,3> vrati help
            help()
        for i in range(2,len(sys.argv)):
            if sys.argv[i].find("-") != -1:
                if sys.argv[i].find("--help") != -1:
                    help()
                if sys.argv[i].find("u") != -1:
                    zapis_debug("prvocisla se ulozi do souboru")
                    ulozit_do_souboru=True
                if sys.argv[i].find("g")  != -1:
                    zapis_debug("prvocisla se budou generovat")
                    generovat_prv=True
                if sys.argv[i].find("n=")  != -1:
                    soubor_prvocislo_n=sys.argv[i][sys.argv[i].find("=")+1:]
                    cisla=nacteni_cisel_soubor(soubor_prvocislo_n)
            elif sys.argv[i].isdigit():
                cisla.append(int(sys.argv[i]))
    else:
        help()
if not cisla:
    help()



zacatek_hlaska=""
if generovat_prv:
    zacatek_hlaska+="generovani"
else:
    zacatek_hlaska += "overovani"
zacatek_hlaska+=" s algoritmem "
match cislo_algoritmu:
    case 1:zacatek_hlaska+="atkinovo sito"
    case 2:zacatek_hlaska+="miller rabin"
    case 3:zacatek_hlaska+="postupne deleni"
zapis_debug("spoustim "+zacatek_hlaska)

cas_Z=time.perf_counter() #spusti casovac

if generovat_prv: #pokud si uzivatel zvolil generovani spusti jeden z algorimtu a bude generovat prvocisla s v rozsahu <2,x)
    match cislo_algoritmu:
        case 1:
            for cislo in cisla:
                prvocisla += atkinovoSito(cislo)
        case 2:
            for cislo in cisla:
                i=2
                while i<cislo:
                    if millerRabin(i):
                        prvocisla.append(i)
                    i+=1
        case 3:
            for cislo in cisla:
                i = 2
                while i < cislo:
                    if postupneDeleni(i):
                        prvocisla.append(i)
                    i += 1
    prvocisla=list(set(prvocisla))
else:       #a zde se pouze overi jestli se jedna o prvocisla zase pomoci zvoleneho algoritmu
    match cislo_algoritmu:
        case 1:
            #protoze tento algoritmus funguje na bazi sita (generuje prvocisla po nejakou hranici),
            # tak zkontrolujeme zda posledni cislo se rovna zadanemu cislu
            for cislo in cisla:
                seznam = atkinovoSito(cislo+1)
                if seznam:
                    if cislo == seznam[len(seznam)-1]:
                        prvocisla.append(cislo)
        case 2:
            for cislo in cisla:
                if millerRabin(cislo):
                    prvocisla.append(cislo)
        case 3:
            for cislo in cisla:
                if postupneDeleni(cislo):
                    prvocisla.append(cislo)
#ukonceni casovace a vrati cas v milisekundach
cas_K = (time.perf_counter() - cas_Z) * 1000
#zapise generovani casu
x="generovani" if generovat_prv else "overovani"
gen_hlaska=f"{x} trvalo:{cas_K:.2f}ms"
print(gen_hlaska)
zapis_debug(gen_hlaska)

#ulozi nebo vytiskne na obrazovku dle toho co si uzivatel zvoli
if ulozit_do_souboru:
    ulozeni_prvocisel_soubor(prvocisla)
else:
    for prvocislo in prvocisla:
        print(prvocislo)
if not prvocisla and not generovat_prv:
    print("žádné z čísel není prvočíslo")

#ulozi cas generovani prvocisel do souboru
#pokud je pocet cifer vetsi nez CIFRY zapise ho ve vedeckem tvaru
CIFRY=10
with open("./prvocisla_cas.log", "a",encoding='utf-8') as time_log:
    operace= "generování" if generovat_prv else "ověřování"
    datum=time.strftime("%H-%M-%S--%d/%m/%Y")
    if not prvocisla:
        prvocislo=-1
    else:
        prvocislo=max(prvocisla)
    if len(str(abs(int(prvocislo)))) >= CIFRY:
        time_log.write(f"datum: {datum} čas: {cas_K:.5f} prvočíslo: {prvocislo:.{CIFRY}e} operace: {operace} algoritmus: {algoritmus[cislo_algoritmu-1]}\n")
    else:
        time_log.write(f"datum: {datum} čas: {cas_K:.5f} prvočíslo: {prvocislo} operace: {operace} algoritmus: {algoritmus[cislo_algoritmu-1]}\n")

debug.close()