num = abs(int(input("Enter an integer: ")))
if num < 10:
    print("Single-digit number")
elif num < 100:
    print("Double-digit number")
elif num < 1000:
    print("Three-digit number")
else:
    print("More than three digits")
