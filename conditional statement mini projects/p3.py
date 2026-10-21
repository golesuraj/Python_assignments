name = input("Enter account holder name: ")
balance = float(input("Enter current balance: "))
withdraw = float(input("Enter withdrawal amount: "))

print("--- ATM Transaction ---")
print("Account Holder Name:", name)

if withdraw <= 0:
    print("Transaction Status: Failed")
    print("Reason: Withdrawal amount must be greater than 0")
elif withdraw > 20000:
    print("Transaction Status: Failed")
    print("Reason: Maximum withdrawal allowed in one transaction is Rs. 20,000")
elif withdraw > balance:
    print("Transaction Status: Failed")
    print("Reason: Insufficient balance")
else:
    remaining_balance = balance - withdraw
    print("Transaction Status: Successful")
    print("Withdrawn Amount: Rs.", withdraw)
    print("Remaining Balance: Rs.", remaining_balance)
    if remaining_balance < 1000:
        print("Warning: Low Balance Warning")
