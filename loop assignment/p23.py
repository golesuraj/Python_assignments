n = int(input("Enter a number: "))
total = 0
temp = abs(n)
while temp > 0:
    digit = temp % 10
    if digit % 2 != 0:
        total += digit
    temp //= 10
print("Sum of odd digits:", total)
