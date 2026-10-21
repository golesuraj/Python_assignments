name = input("Enter customer name: ")
age = int(input("Enter age: "))
risk = input("Enter occupation risk (Low/Medium/High): ")
smoker = input("Are you a smoker (Yes/No): ")

print("--- Insurance Premium Summary ---")
print("Customer Name:", name)

if age < 18:
    print("Eligibility: Not Eligible")
    print("Reason: Age below 18 is not eligible for policy.")
else:
    base_premium = 10000
    additional = 0

    if age > 50:
        additional += 5000

    if risk.lower() == "high":
        additional += 7000
    elif risk.lower() == "medium":
        additional += 3000

    if smoker.lower() == "yes":
        additional += 5000

    final_premium = base_premium + additional

    print("Eligibility: Eligible")
    print("Base Premium: Rs.", base_premium)
    print("Additional Charges: Rs.", additional)
    print("Final Premium: Rs.", final_premium)

    if additional >= 10000:
        print("Risk Message: High Risk Policy")
