s = input("Enter a string: ")
letters = ""
for ch in s:
    if ch.isalpha():
        letters += ch
print("Alphabets:", letters)
