s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1
print("Number of consonants:", count)
