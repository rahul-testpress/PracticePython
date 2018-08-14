n = int(input("Enter the amount of fibonacci numbers to generate : "))
a, b = 0, 1
if n > 0:
    fibonacci_numbers = [b]
    for i in range(1, n):
        c = a + b
        fibonacci_numbers.append(c)
        a = b
        b = c
    print(fibonacci_numbers)
else:
    print("Invalid limit")
