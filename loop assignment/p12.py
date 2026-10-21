n = int(input("Enter a number: "))
rev = 0
temp = n
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print("Reversed number:", rev)
