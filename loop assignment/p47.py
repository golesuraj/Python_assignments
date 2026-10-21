n = int(input("Enter a number: "))
temp = abs(n)
prod = 1
if temp == 0:
    prod = 0
while temp > 0:
    prod *= (temp % 10)
    temp //= 10
print("Product of digits:", prod)
