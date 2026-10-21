s = input("Enter a string: ")
res = ""
for ch in s:
    if ch not in res:
        res += ch
print(res)
