s = input("Enter a string: ")
sub = input("Enter substring: ")
if s.startswith(sub):
    print("Yes, starts with", sub)
else:
    print("No, does not start with", sub)
