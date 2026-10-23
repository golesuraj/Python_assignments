amount = float(input("Enter total shopping amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0.0
final_amount = amount - discount
print("Discount:", discount)
print("Final Amount:", final_amount)
