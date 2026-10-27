print("=" * 55)
print("             BANK TRANSACTION HISTORY")
print("=" * 55)

while True:
    try:
        current_balance = float(input("Enter opening balance (Rs.): "))
        if current_balance >= 0:
            break
        print("Opening balance cannot be negative.")
    except ValueError:
        print("Invalid input! Please enter a numeric amount.")

while True:
    try:
        num_transactions = int(input("Enter total number of transactions: "))
        if num_transactions >= 0:
            break
        print("Number of transactions must be 0 or positive.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

deposit_count = 0
successful_withdrawal_count = 0
rejected_withdrawal_count = 0

print("\n--- Enter Transactions ---")
for i in range(1, num_transactions + 1):
    print(f"\nTransaction #{i}:")
    
    while True:
        trans_type = input("  Enter type ('D' for Deposit / 'W' for Withdrawal): ").strip().upper()
        if trans_type in ["D", "W"]:
            break
        print("  Invalid selection! Please enter 'D' or 'W'.")

    while True:
        try:
            amount = float(input("  Enter amount (Rs.): "))
            if amount > 0:
                break
            print("  Amount must be greater than 0.")
        except ValueError:
            print("  Invalid input! Please enter a numeric amount.")

    if trans_type == "D":
        current_balance += amount
        deposit_count += 1
        print(f"  Status: SUCCESS! Deposited Rs. {amount:.2f}. Balance: Rs. {current_balance:.2f}")
    else:
        if amount <= current_balance:
            current_balance -= amount
            successful_withdrawal_count += 1
            print(f"  Status: SUCCESS! Withdrew Rs. {amount:.2f}. Balance: Rs. {current_balance:.2f}")
        else:
            rejected_withdrawal_count += 1
            print(f"  Status: REJECTED! Insufficient funds. Available: Rs. {current_balance:.2f}")

print("\n" + "=" * 55)
print("             ACCOUNT ACTIVITY SUMMARY")
print("=" * 55)
print(f"Total Transactions Processed : {num_transactions}")
print(f"Successful Deposits          : {deposit_count}")
print(f"Successful Withdrawals       : {successful_withdrawal_count}")
print(f"Rejected Withdrawals         : {rejected_withdrawal_count}")
print(f"Final Balance                : Rs. {current_balance:.2f}")

if current_balance < 1000:
    print("\nWARNING: Low balance alert! Your balance is below Rs. 1,000.")
print("=" * 55)
