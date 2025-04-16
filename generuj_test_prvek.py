import matplotlib.pyplot as plt

target = 3317044064679887385961981
numbers = []
n = 1
step = 1.1  # Growth factor
last_int = 0

while n < target:
    current_int = int(n)
    if current_int > last_int:
        numbers.append(current_int)
        last_int = current_int
    n *= step

# Save to file
with open("numbers.txt", "w") as f:
    for number in numbers:
        f.write(f"{number}\n")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(len(numbers)), numbers)
plt.title("Generated Numbers with Increasing Spacing")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.tight_layout()
plt.show()
