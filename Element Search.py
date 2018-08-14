from random import randint

sorted_list_of_numbers = []

for i in range(0, int(input("Enter the length of list : "))):
    # add random values to the lists
    sorted_list_of_numbers.append(randint(0, 100))
sorted_list_of_numbers.sort()
n = int(input("Enter the number to search in list : "))


def binary_search(list_of_numbers, number_to_search):
    start_pos = 0
    end_pos = len(list_of_numbers) - 1

    while start_pos != end_pos and end_pos - start_pos > 1:

        if number_to_search == list_of_numbers[(start_pos + end_pos) // 2]:
            return True
        elif number_to_search > list_of_numbers[(start_pos + end_pos) // 2]:
            start_pos = (start_pos + end_pos) // 2
        elif number_to_search < list_of_numbers[(start_pos + end_pos) // 2]:
            end_pos = (start_pos + end_pos) // 2
    if list_of_numbers[start_pos] == number_to_search or list_of_numbers[end_pos] == number_to_search:
        return True


if binary_search(sorted_list_of_numbers, n):
    print("Element is present in the list")
else:
    print("Element is not present in the list")
