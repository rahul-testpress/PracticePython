import random

a = []
b = []

for i in range(0, 25):
    # add random values to the lists
    a.append(random.randint(0, 100))
print("The list is : {}".format(a))
n = int(input("Enter the number to compare from the above list : "))
for i in a:
    if i < n:
        b.append(i)
b.sort()
print("List of numbers smaller than {0} is {1}".format(n, b))
