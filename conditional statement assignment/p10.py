name = input("Enter customer name: ")
bill = float(input("Enter food bill amount: "))
membership = input("Do you have membership (Yes/No): ")

if bill >= 5000:
    discount_pct = 15
elif bill >= 3000:
    discount_pct = 10
elif bill >= 1000:
    discount_pct = 5
else:
    discount_pct = 0

if membership.lower() == "yes":
    discount_pct += 5

discount_amount = (bill * discount_pct) / 100
after_discount = bill - discount_amount

service_charge = after_discount * 0.05
final_payable = after_discount + service_charge

print("--- Restaurant Bill ---")
print("Customer Name:", name)
print("Original Bill: Rs.", bill)
print("Discount: Rs.", discount_amount)
print("Service Charge (5%): Rs.", service_charge)
print("Final Payable Amount: Rs.", final_payable)

if final_payable >= 5000:
    print("Message: Thank you for being a valued customer")
