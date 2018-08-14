n = int(input("Enter any number : "))
list_of_divisors = []
for i in range(1, (n//2) + 1):
    if n % i == 0:
        list_of_divisors.append(i)
list_of_divisors.append(n)
print("Divisors of {0} are {1}".format(n, list_of_divisors))
