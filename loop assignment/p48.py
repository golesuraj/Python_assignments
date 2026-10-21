n = int(input("Enter a number: "))
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    temp //= 10
if total == n and n > 0:
    print("Strong number")
else:
    print("Not a strong number")
