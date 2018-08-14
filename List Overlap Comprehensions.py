import random

a = []
b = []
for i in range(0, 20):
    # add random values to the lists
    a.append(random.randint(0, 20))
    b.append(random.randint(0, 20))
print("List 1 : {}".format(a))
print("List 2 : {}".format(b))
common_elements = sorted(list(set([i for i in b if i in a])))
print("\nCommon elements in List1 and List2 : {}".format(common_elements))
