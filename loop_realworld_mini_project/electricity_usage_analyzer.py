# Mini Project 6: Electricity Usage Analyzer
# Problem Statement: Analyze daily electricity consumption over a selected period.

print("=" * 50)
print("        ELECTRICITY USAGE ANALYZER")
print("=" * 50)

# Input validation for number of days
while True:
    try:
        num_days = int(input("Enter number of days to analyze: "))
        if num_days > 0:
            break
        print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

total_units = 0.0
high_usage_day_count = 0
max_daily_usage = 0.0

print("\n--- Enter Daily Units Consumed ---")
for day in range(1, num_days + 1):
    while True:
        try:
            units = float(input(f"Enter units consumed for Day {day}: "))
            if units >= 0:
                break
            print("Units cannot be negative. Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # Accumulate total
    total_units += units

    # Count days with usage greater than 10 units
    if units > 10:
        high_usage_day_count += 1

    # Track maximum daily usage
    if day == 1 or units > max_daily_usage:
        max_daily_usage = units

# Calculate average usage
average_units = total_units / num_days

# Determine overall usage status
if total_units > 300:
    usage_status = "High Usage"
else:
    usage_status = "Normal Usage"

# Display Summary Output
print("\n" + "=" * 50)
print("            CONSUMPTION SUMMARY")
print("=" * 50)
print(f"Total Days Analyzed       : {num_days}")
print(f"Total Units Consumed      : {total_units:.2f} units")
print(f"Average Daily Usage       : {average_units:.2f} units")
print(f"High-Usage Days (>10 units: {high_usage_day_count} day(s)")
print(f"Maximum Daily Usage       : {max_daily_usage:.2f} units")
print(f"Usage Status              : {usage_status}")
if total_units > 300:
    print("Alert: Total electricity consumption exceeded 300 units!")
print("=" * 50)
