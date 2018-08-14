import random

a = []
b = []
for i in range(0, 25):
    # add random values to the lists
    a.append(random.randint(0, 100))
    b.append(random.randint(0, 100))
common_elements_list = set()
for i in a:
    if i in b:
        common_elements_list.add(i)
print("List 1 : {}".format(a))
print("List 2 : {}".format(b))
print("\nCommon elements in both lists are : {}".format(sorted(list(common_elements_list))))
