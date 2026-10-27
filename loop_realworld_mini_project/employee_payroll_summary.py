print("=" * 60)
print("             EMPLOYEE PAYROLL SUMMARY")
print("=" * 60)

while True:
    try:
        num_employees = int(input("Enter number of employees: "))
        if num_employees > 0:
            break
        print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

OVERTIME_RATE = 200.0
total_net_payroll = 0.0

print("\n--- Processing Employee Payroll ---")
for i in range(1, num_employees + 1):
    print(f"\nEmployee #{i}:")
    name = input("  Enter employee name: ").strip()
    while not name:
        name = input("  Name cannot be empty. Enter name: ").strip()

    while True:
        try:
            basic_salary = float(input("  Enter basic salary (Rs.): "))
            if basic_salary >= 0:
                break
            print("  Salary cannot be negative. Try again.")
        except ValueError:
            print("  Invalid input! Enter a valid salary amount.")

    while True:
        try:
            ot_hours = float(input("  Enter overtime hours worked: "))
            if ot_hours >= 0:
                break
            print("  Overtime hours cannot be negative. Try again.")
        except ValueError:
            print("  Invalid input! Enter a valid number of hours.")

    overtime_pay = ot_hours * OVERTIME_RATE
    gross_salary = basic_salary + overtime_pay

    if gross_salary >= 50000:
        deduction_rate = 0.10
    else:
        deduction_rate = 0.05

    deduction = gross_salary * deduction_rate
    net_salary = gross_salary - deduction

    total_net_payroll += net_salary

    print(f"  --> Gross Salary : Rs. {gross_salary:.2f}")
    print(f"  --> Deduction ({int(deduction_rate * 100)}%): Rs. {deduction:.2f}")
    print(f"  --> Net Salary   : Rs. {net_salary:.2f}")

print("\n" + "=" * 60)
print("             PAYROLL GRAND SUMMARY")
print("=" * 60)
print(f"Total Employees Processed : {num_employees}")
print(f"Total Net Payroll Outflow : Rs. {total_net_payroll:.2f}")
print("=" * 60)
