import os
import re
import time

algoritmus = ("atkinovoSito","millerRabin","postupneDeleni")
al_c=2
konec=False
i=0
cisla=[]
souradnice=[]
radek=0
if os.path.isfile("posledni_radek"):
    with open("posledni_radek","r") as t:
        try:
            radek=int(t.read())
        except:
            radek=0

print(radek)

with open("cisla_test.txt","r") as t:
    cisla=(t.readlines())

for i in range(0,len(cisla)):
    cisla[i]=int(cisla[i])
print("lol")
print(cisla)

for i in range(radek, len(cisla)):
    try:
        print(f"python3 gop.py {al_c} {cisla[i]}")
        os.system(f"python3 gop.py {al_c} {cisla[i]}")
        with open("prvocisla_cas.log", "r", encoding="utf-8") as t:
            radky = t.readlines()
            if not radky:
                print("Soubor je prázdný.")
            else:
                posledni_radek = radky[-1]

                # Najdi čas v posledním řádku
                match = re.search(r"čas:\s*([\d\.]+)", posledni_radek)
                if match:
                    cas = float(match.group(1))
                    souradnice.append([cas,cisla[i]])
        time.sleep(0.2)
        if konec:break
    except KeyboardInterrupt:
        print("sus")
        konec=True



with open("posledni_radek","w") as t:
    t.write(str(i))
with open("cas_vykon"+algoritmus[al_c-1],"a+") as c:
    for xy in souradnice:
        c.write(str(xy)+"\n")

