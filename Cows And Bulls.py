from random import randint

cows = 0
bulls = 0
random_number = str(randint(1000, 9999))
print(random_number)
input_number = input("Guess any 4 digit number: ")


def check_equality():
    global cows, bulls, input_number
    cows = bulls = 0
    random_number_list = [i for i in random_number]
    input_number_list = [i for i in input_number]
    for i in range(0, 4):
        if random_number_list[i] in input_number_list:
            if input_number_list[i] == random_number_list[i]:
                cows += 1
            else:
                bulls += 1
        input_number_list[i] = ""
    print("{0} cows and {1} bulls".format(cows, bulls))
    input_number = input("Guess again : ")


while input_number != random_number and (999 < int(input_number) <= 9999):
    check_equality()
else:
    if int(input_number) >= 10000 or int(input_number) < 1000:
        print("Please enter a 4 digit number only")
    elif input_number == random_number:
        print("Correct guess")
