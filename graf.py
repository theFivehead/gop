
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import ylabel, xlabel
from matplotlib.ticker import MultipleLocator

'''
# Define a range for n from 10^3 to 10^8
n = np.logspace(3, 8, num=500)

# Heuristic models (arbitrary constant factors omitted)
f_trial = np.sqrt(n)        # O(sqrt(n))
f_atkin = n                 # O(n)
f_mr = (np.log(n))**3       # O((log n)^3)

plt.figure(figsize=(8,6))
plt.loglog(n, f_trial, label="Postupné dělení O(√n)")
plt.loglog(n, f_atkin, label="Atkinovo Síto O(n)")
plt.loglog(n, f_mr, label="Miller–Rabin O((log n)³)")

plt.xlabel("n")
plt.ylabel("Předpokládané operace")
plt.title("Asymptotická složitost")
plt.legend()
plt.savefig("predpoklad.png",dpi=900)
'''



algoritmus = ("atkinovoSito","millerRabin","postupneDeleni")

font=15
for alg in algoritmus:
    ykrok = 0.2
    xkrok=1e6
    soubour = ""
    souradnice = []
    print(alg)
    try:
        with open("cas_vykon"+alg) as f:
            soubour=f.read()
    except:
        continue

    soubour=soubour.replace("[","")
    soubour=soubour.replace("]","")
    soubour=soubour.split("\n")
    for data in soubour:
        if not data:continue
        souradnice.append(data.split(","))
    if not souradnice:
        continue
    x=[0.0]*(len(souradnice))
    y=[0.0]*(len(souradnice))

    #souradnice.sort(key = lambda e: e[1])
    #print(souradnice)

    for i in range(0,len(souradnice)-1):
        x[i]=float(souradnice[i][1])
        y[i]=float(souradnice[i][0])

    #print(soubour)
    #print(souradnice)

    plt.figure(figsize=(18, 8))

    x.sort()
    y.sort()

    print(max(x))
    print(max(y))
    ymargin=0.5
    ax = plt.gca()
    if max(y) > 1000:
        for i in range(0,len(y)):
            y[i]=y[i]/1000
        ylabel("čas(s)").set_fontsize(font)
        ykrok = 1
        if max(y)>100:
            ykrok=5

        elif max(y)>60000:
            ykrok=5
    else:
        ylabel("čas(ms)").set_fontsize(font)
        ykrok=0.01
        ymargin=0.1
    if max(x) > 1e2:
        xkrok=10 ** (np.floor(np.log10(max(x))) - 1)
        xlabel(f"čísla({xkrok:.{1}e})").set_fontsize(font)

    else:
        xlabel("čísla(1e6)").set_fontsize(font)
    plt.xlim(0, max(x))
    plt.ylim(min(y), max(y) + ymargin)


    print(xkrok)
    ax.xaxis.set_major_locator(MultipleLocator(xkrok))
    ax.yaxis.set_major_locator(MultipleLocator(ykrok))




    plt.plot(x, y)

    '''
    # Hide every second y-axis label
    for label in ax.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)
    '''
    #plt.show()
    plt.savefig(alg+'.png', dpi=900)