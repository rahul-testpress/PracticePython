try:
    n = int(input("Enter any number : "))
    if n % 2 == 0:
        if n % 4 == 0:
            print("The number entered is even and a multiple of 4")
        else:
            print("The number entered is even")
    elif n % 2 == 1:
        print("The number entered is odd")
except:
    print("Invalid input")
