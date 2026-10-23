units = float(input("Enter electricity units consumed: "))
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)
else:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)
print("Electricity Bill: Rs.", bill)
