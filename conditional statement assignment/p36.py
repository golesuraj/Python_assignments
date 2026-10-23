age = int(input("Enter age: "))
test_status = input("Passed driving test (yes/no): ").strip().lower()
if age >= 18 and test_status == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")
