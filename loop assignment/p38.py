n = int(input("Enter a number: "))
temp = abs(n)
smallest = 9
if temp == 0:
    smallest = 0
while temp > 0:
    digit = temp % 10
    if digit < smallest:
        smallest = digit
    temp //= 10
print("Smallest digit:", smallest)
