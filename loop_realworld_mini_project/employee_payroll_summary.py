# Mini Project 7: Employee Payroll Summary
# Problem Statement: Calculate payroll details for several employees.

print("=" * 60)
print("             EMPLOYEE PAYROLL SUMMARY")
print("=" * 60)

# Input validation for number of employees
while True:
    try:
        num_employees = int(input("Enter number of employees: "))
        if num_employees > 0:
            break
        print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

OVERTIME_RATE = 200.0  # Rs. 200 per hour
total_net_payroll = 0.0

print("\n--- Processing Employee Payroll ---")
for i in range(1, num_employees + 1):
    print(f"\nEmployee #{i}:")
    name = input("  Enter employee name: ").strip()
    while not name:
        name = input("  Name cannot be empty. Enter name: ").strip()

    # Validate basic salary
    while True:
        try:
            basic_salary = float(input("  Enter basic salary (Rs.): "))
            if basic_salary >= 0:
                break
            print("  Salary cannot be negative. Try again.")
        except ValueError:
            print("  Invalid input! Enter a valid salary amount.")

    # Validate overtime hours
    while True:
        try:
            ot_hours = float(input("  Enter overtime hours worked: "))
            if ot_hours >= 0:
                break
            print("  Overtime hours cannot be negative. Try again.")
        except ValueError:
            print("  Invalid input! Enter a valid number of hours.")

    # Calculations
    overtime_pay = ot_hours * OVERTIME_RATE
    gross_salary = basic_salary + overtime_pay

    # Deductions: 10% if gross salary >= 50,000, else 5%
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

# Display Company-wide Summary
print("\n" + "=" * 60)
print("             PAYROLL GRAND SUMMARY")
print("=" * 60)
print(f"Total Employees Processed : {num_employees}")
print(f"Total Net Payroll Outflow : Rs. {total_net_payroll:.2f}")
print("=" * 60)
