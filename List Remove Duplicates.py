import random


def duplicate_removal(input_list):
    input_list = list(set(input_list))
    return input_list


sample_list = []

for i in range(0, 25):
    # add random values to the lists
    sample_list.append(random.randint(0, 100))

print("Original list : {}".format(sorted(sample_list)))
print("List without duplicate items : {}".format(sorted(duplicate_removal(sample_list))))
