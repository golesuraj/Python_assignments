base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
res = 1
for _ in range(exp):
    res *= base
print("Result:", res)
