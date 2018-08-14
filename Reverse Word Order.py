def reverse_string(string_to_reverse):
    # Reverse the string passed in param
    split_string_list = string_to_reverse.split(" ")
    reversed_string = [split_string_list[i] for i in range(len(split_string_list)-1, -1, -1)]
    split_string_list = " ".join(reversed_string)
    return split_string_list


input_string = input("Enter any string: ")
print("Reversed String : {}".format(reverse_string(input_string)))

