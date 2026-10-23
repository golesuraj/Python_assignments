service_years = float(input("Enter years of service: "))
salary = float(input("Enter salary: "))
if service_years > 5:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05
print("Bonus:", bonus)
