import numpy as np
import matplotlib.pyplot as plt

# Define a range for n from 10^3 to 10^8
n = np.logspace(3, 8, num=500)

# Heuristic models (arbitrary constant factors omitted)
f_trial = np.sqrt(n)        # O(sqrt(n))
f_atkin = n                 # O(n)
f_mr = (np.log(n))**3       # O((log n)^3)

plt.figure(figsize=(8,6))
plt.loglog(n, f_trial, label="Trial Division O(√n)")
plt.loglog(n, f_atkin, label="Sieve of Atkin O(n)")
plt.loglog(n, f_mr, label="Miller–Rabin O((log n)³)")

plt.xlabel("n")
plt.ylabel("Estimated Operations (arb. units)")
plt.title("Heuristic Time Complexities")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
