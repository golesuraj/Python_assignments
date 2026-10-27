# Mini Project 2: Student Marks and Grade Report
# Problem Statement: Process marks for multiple students and generate a class performance summary.

print("=" * 50)
print("       STUDENT MARKS AND GRADE REPORT")
print("=" * 50)

# Input validation for number of students
while True:
    try:
        num_students = int(input("Enter number of students: "))
        if num_students > 0:
            break
        print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

total_marks = 0.0
pass_count = 0
fail_count = 0

print("\n--- Enter Student Details ---")
for i in range(1, num_students + 1):
    name = input(f"\nEnter name of Student {i}: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter student name: ").strip()

    # Reject marks outside 0-100
    while True:
        try:
            marks = float(input(f"Enter marks for {name} (0-100): "))
            if 0 <= marks <= 100:
                break
            print("Invalid marks! Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # Determine grade
    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Count pass and fail students
    if grade != "Fail":
        pass_count += 1
    else:
        fail_count += 1

    total_marks += marks

    print(f"Result for {name}: Marks = {marks:.2f}, Grade = {grade}")

# Calculate class average
class_average = total_marks / num_students

# Display summary report
print("\n" + "=" * 50)
print("            CLASS PERFORMANCE SUMMARY")
print("=" * 50)
print(f"Total Students  : {num_students}")
print(f"Class Average   : {class_average:.2f}")
print(f"Pass Count      : {pass_count}")
print(f"Fail Count      : {fail_count}")
print("=" * 50)
