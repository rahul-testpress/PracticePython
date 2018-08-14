import random
import string

strong_password_letters = string.ascii_letters + string.punctuation + string.digits
choice = input("Enter the type of password required : Press W for weak or S for strong : ").upper()
if choice == "W":
    print("".join(random.sample(string.ascii_letters, 6)))
elif choice == "S":
    print("".join(random.sample(strong_password_letters, 8)))
else:
    print("Invalid choice")
