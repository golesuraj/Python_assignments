import string

s = input("Enter a string: ")
res = ""
for ch in s:
    if ch not in string.punctuation:
        res += ch
print(res)
