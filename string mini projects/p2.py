password = input("Enter a password to check: ")

length_ok = len(password) >= 8
has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif not ch.isalnum() and not ch.isspace():
        has_special = True

score = 0
if length_ok:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

print("\n--- Password Evaluation ---")
if length_ok:
    print("Length (>= 8 chars): Yes")
else:
    print("Length (>= 8 chars): No")

if has_upper:
    print("Has Uppercase Letter: Yes")
else:
    print("Has Uppercase Letter: No")

if has_lower:
    print("Has Lowercase Letter: Yes")
else:
    print("Has Lowercase Letter: No")

if has_digit:
    print("Has Digit: Yes")
else:
    print("Has Digit: No")

if has_special:
    print("Has Special Character: Yes")
else:
    print("Has Special Character: No")

if score == 5:
    strength = "Strong"
elif score >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print("Password Strength:", strength)
