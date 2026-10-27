print("=" * 45)
print("       DAILY EXPENSE TRACKER")
print("=" * 45)

while True:
    try:
        num_days = int(input("Enter number of days to track: "))
        if num_days > 0:
            break
        print("Please enter a valid positive number of days (greater than 0).")
    except ValueError:
        print("Invalid input! Please enter an integer.")

total_expense = 0.0
highest_expense = 0.0

for day in range(1, num_days + 1):
    while True:
        try:
            expense = float(input(f"Enter expense for Day {day} (in Rs.): "))
            if expense >= 0:
                break
            print("Expense cannot be negative. Please enter a valid amount.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    total_expense += expense
    
    if day == 1 or expense > highest_expense:
        highest_expense = expense

average_expense = total_expense / num_days

budget_status = "Budget Alert" if total_expense > 5000 else "Within Budget"

print("\n" + "=" * 45)
print("           EXPENSE SUMMARY")
print("=" * 45)
print(f"Total Expense         : Rs. {total_expense:.2f}")
print(f"Average Daily Expense : Rs. {average_expense:.2f}")
print(f"Highest Daily Expense : Rs. {highest_expense:.2f}")
print(f"Budget Status         : {budget_status}")
if total_expense > 5000:
    print("Warning: Total spending exceeded Rs. 5,000!")
print("=" * 45)
