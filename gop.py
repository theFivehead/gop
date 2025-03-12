import time
import itertools
import timeit
from multiprocessing import Process, cpu_count
from idlelib.configdialog import is_int

#definovani promennych --------------------------------------------------------------------------
soubor_prvocislo="prvocisla.txt"
testovat_prvociselnost=True

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

def erastenovoSito():
    pass

def millerRabin():
    pass

def AKS():
    pass



print("chcete otestova prvocislo")

test=nacteni_cisel_soubor(soubor_prvocislo)
print(test)
ulozeni_prvocisel_soubor(test)
