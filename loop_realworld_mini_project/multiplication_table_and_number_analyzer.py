# Mini Project 10: Multiplication Table and Number Analyzer
# Problem Statement: Print a multiplication table and analyze a range of integers.

print("=" * 55)
print("     MULTIPLICATION TABLE & NUMBER ANALYZER")
print("=" * 55)

# Part 1: Input and Table Generation
while True:
    try:
        table_num = int(input("Enter a positive integer for multiplication table: "))
        if table_num > 0:
            break
        print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

print(f"\n--- Multiplication Table for {table_num} (1 to 10) ---")
for i in range(1, 11):
    product = table_num * i
    print(f"{table_num:2d} x {i:2d} = {product:3d}")

# Part 2: Number Range Analysis
print("\n" + "-" * 55)
print("                 RANGE ANALYZER")
print("-" * 55)

# Input and validation: start must not be greater than end
while True:
    try:
        start_val = int(input("Enter start of number range: "))
        end_val = int(input("Enter end of number range: "))
        if start_val <= end_val:
            break
        print("Validation Error: Start value cannot be greater than end value. Try again.\n")
    except ValueError:
        print("Invalid input! Please enter valid integers.\n")

even_count = 0
odd_count = 0
range_sum = 0

# Loop through each integer in range [start_val, end_val]
for num in range(start_val, end_val + 1):
    range_sum += num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display summary report
print("\n" + "=" * 55)
print("                 ANALYSIS REPORT")
print("=" * 55)
print(f"Number Range Analyzed : [{start_val} to {end_val}]")
print(f"Even Numbers Count    : {even_count}")
print(f"Odd Numbers Count     : {odd_count}")
print(f"Sum of Range Numbers  : {range_sum}")
print("=" * 55)
