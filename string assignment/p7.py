s = input("Enter a string: ")
sub = input("Enter substring: ")
if s.endswith(sub):
    print("Yes, ends with", sub)
else:
    print("No, does not end with", sub)
