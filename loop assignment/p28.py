n = int(input("Enter a number: "))
num_digits = len(str(n))
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** num_digits
    temp //= 10
if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
