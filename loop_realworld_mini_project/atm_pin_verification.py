# Mini Project 3: ATM PIN Verification
# Problem Statement: Simulate ATM access with a limited number of PIN attempts.

print("=" * 45)
print("            ATM PIN VERIFICATION")
print("=" * 45)

CORRECT_PIN = "5432"
MAX_ATTEMPTS = 3
attempts_used = 0
access_granted = False

# While loop for limited attempts
while attempts_used < MAX_ATTEMPTS:
    entered_pin = input(f"Enter your 4-digit PIN (Attempt {attempts_used + 1}/{MAX_ATTEMPTS}): ").strip()
    attempts_used += 1

    if entered_pin == CORRECT_PIN:
        access_granted = True
        print("\n>> Access Granted! Welcome to your account. <<")
        break
    else:
        remaining = MAX_ATTEMPTS - attempts_used
        if remaining > 0:
            print(f"Incorrect PIN. You have {remaining} attempt(s) remaining.\n")

# Display status and summary
print("\n" + "=" * 45)
print("            TRANSACTION STATUS")
print("=" * 45)
if access_granted:
    print("Access Status : Access Granted")
    print(f"Attempts Used : {attempts_used}")
else:
    print("Access Status : Access Denied")
    print(f"Attempts Used : {attempts_used}")
    print("Alert         : Card Temporarily Locked")
    print("Please contact customer support to unlock your card.")
print("=" * 45)
