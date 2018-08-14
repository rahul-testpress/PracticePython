st = input("Enter any String of characters : ").upper()
counter = 0

for i in range(0, len(st)):
    if st[i] == st[len(st)-i-1]:
        counter += 1
if counter == len(st):
    print("Palindrome")
else:
    print("not a Palindrome")
