s = input("Enter a string: ")
if s.lower() == s.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
