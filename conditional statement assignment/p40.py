password = input("Enter password: ")
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            print("Valid password")
        else:
            print("Password must contain at least one uppercase letter")
    else:
        print("Password must contain at least one digit")
else:
    print("Password must have at least 8 characters")
