n = int(input("Enter a number: "))
temp = abs(n)
largest = 0
while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp //= 10
print("Largest digit:", largest)
