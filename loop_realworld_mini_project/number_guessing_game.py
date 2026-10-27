# Mini Project 5: Number Guessing Game
# Problem Statement: Give the user a limited number of chances to guess a secret number.

print("=" * 45)
print("          NUMBER GUESSING GAME")
print("=" * 45)
print("I have chosen a secret number between 1 and 100.")
print("You have 5 attempts to guess it correctly!\n")

SECRET_NUMBER = 37
MAX_ATTEMPTS = 5
attempts_used = 0
guessed_correctly = False

# While loop for limited guess attempts
while attempts_used < MAX_ATTEMPTS:
    try:
        guess = int(input(f"Enter guess #{attempts_used + 1}: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        continue

    attempts_used += 1

    if guess == SECRET_NUMBER:
        guessed_correctly = True
        print("\n>> Congratulations! You guessed the correct number! <<")
        break
    elif guess < SECRET_NUMBER:
        print("Hint: Too low!")
    else:
        print("Hint: Too high!")

    remaining = MAX_ATTEMPTS - attempts_used
    if remaining > 0:
        print(f"Chances left: {remaining}\n")

# Final result summary
print("\n" + "=" * 45)
print("               GAME RESULT")
print("=" * 45)
if guessed_correctly:
    print("Outcome       : YOU WON!")
    print(f"Attempts Used : {attempts_used}")
else:
    print("Outcome       : YOU LOST! Out of attempts.")
    print(f"Attempts Used : {attempts_used}")
    print(f"Secret Number : {SECRET_NUMBER}")
print("=" * 45)
