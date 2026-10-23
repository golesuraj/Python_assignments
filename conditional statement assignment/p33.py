age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
if age >= 21 and income >= 25000 and credit_score >= 700:
    print("Eligible to apply for loan")
else:
    print("Not eligible to apply for loan")
