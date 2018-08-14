import random

generated_number = random.randint(0, 9)
user_input = input("Guess a number between 0 and 9 : ")
no_of_guesses = 0

while user_input != "exit":
    no_of_guesses += 1
    guessed_number = int(user_input)
    if guessed_number == generated_number:
        print("Correct guess in {} attempts".format(no_of_guesses))
        break
    elif guessed_number < generated_number:
        print("Guess is low \n")
    elif guessed_number > generated_number:
        print("Guess is high \n")
    user_input = input("Guess again or type 'exit' to stop playing: ")
