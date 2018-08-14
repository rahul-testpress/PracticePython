import random

a = []

for i in range(0, 25):
    # add random values to the lists
    a.append(random.randint(0, 100))
print("The List is : {}".format(a))
b = sorted([j for j in a if j % 2 == 0])
print("Even numbers in above list are : {}".format(b))
