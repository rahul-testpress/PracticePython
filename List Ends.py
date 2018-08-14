import random

a = []

for i in range(0, 25):
    # add random values to the lists
    a.append(random.randint(0, 100))
print(a)
b = [a[i] for i in range(0, len(a)) if i == 0 or i == len(a)-1]
print(b)
