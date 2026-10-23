balance = 10000.0
choice = int(input("ATM Menu:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\nEnter choice (1-4): "))
match choice:
    case 1:
        print("Current Balance: Rs.", balance)
    case 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Updated Balance: Rs.", balance)
    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. Remaining Balance: Rs.", balance)
        else:
            print("Insufficient balance")
    case 4:
        print("Thank you for visiting.")
    case _:
        print("Invalid choice")
