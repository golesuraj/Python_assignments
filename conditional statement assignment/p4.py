name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
income = float(input("Enter annual family income: "))
attendance = float(input("Enter attendance percentage: "))

print("--- Scholarship Eligibility Result ---")
print("Student Name:", name)

if percentage >= 75 and income <= 400000 and attendance >= 75:
    print("Eligibility Status: Eligible")
    if percentage >= 90:
        print("Scholarship Category: Full Scholarship")
    else:
        print("Scholarship Category: Partial Scholarship")
else:
    print("Eligibility Status: Not Eligible")
    print("Scholarship Category: None")
    if percentage < 75:
        print("Reason: Percentage is less than 75%")
    elif income > 400000:
        print("Reason: Annual family income exceeds Rs. 4,00,000")
    elif attendance < 75:
        print("Reason: Attendance is less than 75%")
