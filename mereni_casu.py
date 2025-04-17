import os
import time
i=0
cisla=[]
radek=0
if os.path.isfile("posledni_radek"):
    with open("posledni_radek","r") as f:
        try:
            radek=int(f.read())
        except:
            radek=0

print(radek)

with open("cisla_test.txt","r") as f:
    cisla=(f.readlines())

for i in range(0,len(cisla)):
    cisla[i]=int(cisla[i])

print(cisla)
try:
    for i in range(radek, len(cisla)):
        time.sleep(0.2)
        os.system(f"gop.py 2 {cisla[i]}")
except KeyboardInterrupt:
    with open("posledni_radek","w") as f:
        f.write(str(i))


