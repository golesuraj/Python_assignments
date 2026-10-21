s = input("Enter a string: ")
digits = ""
for ch in s:
    if ch.isdigit():
        digits += ch
print("Digits:", digits)
