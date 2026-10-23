attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter internal marks: "))
if attendance >= 75:
    if marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible due to low marks")
else:
    print("Not eligible due to low attendance")
