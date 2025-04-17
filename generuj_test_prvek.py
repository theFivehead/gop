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
with open("cisla_test.txt", "w") as f:
    for number in numbers:
        f.write(f"{number}\n")

