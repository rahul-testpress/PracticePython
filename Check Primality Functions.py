n = int(input("Enter any number to check its primality : "))


def no_of_divisors(num):
    list_of_divisors = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            list_of_divisors.append(i)
    list_of_divisors.append(num)
    return len(list_of_divisors)


count = no_of_divisors(n)
if count == 2:
    print("Prime")
else:
    print("Non Prime")
