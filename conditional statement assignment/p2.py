name = input("Enter customer name: ")
amount = float(input("Enter purchase amount: "))
cust_type = input("Enter customer type (Regular/Premium): ")

if amount >= 5000:
    discount_rate = 20
elif amount >= 3000:
    discount_rate = 10
elif amount >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

if cust_type.lower() == "premium":
    discount_rate += 5

discount_amount = (amount * discount_rate) / 100
amount_after_discount = amount - discount_amount

if amount_after_discount >= 2000:
    delivery_charge = 0
else:
    delivery_charge = 100

final_amount = amount_after_discount + delivery_charge

print("--- Checkout Details ---")
print("Customer Name:", name)
print("Discount Amount: Rs.", discount_amount)
print("Delivery Charge: Rs.", delivery_charge)
print("Final Payable Amount: Rs.", final_amount)
