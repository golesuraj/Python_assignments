print("=" * 45)
print("            SHOPPING CART BILLING")
print("=" * 45)

while True:
    try:
        num_products = int(input("Enter number of products: "))
        if num_products > 0:
            break
        print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

subtotal = 0.0

print("\n--- Enter Product Details ---")
for i in range(1, num_products + 1):
    print(f"\nProduct #{i}:")
    
    while True:
        try:
            price = float(input("  Enter price (Rs.): "))
            if price >= 0:
                break
            print("  Price cannot be negative. Try again.")
        except ValueError:
            print("  Invalid input! Enter a valid price.")

    while True:
        try:
            qty = int(input("  Enter quantity: "))
            if qty > 0:
                break
            print("  Quantity must be at least 1. Try again.")
        except ValueError:
            print("  Invalid input! Enter an integer for quantity.")

    item_total = price * qty
    subtotal += item_total
    print(f"  Item Subtotal: Rs. {item_total:.2f}")

if subtotal >= 3000:
    discount = subtotal * 0.10
else:
    discount = 0.0

discounted_amount = subtotal - discount

if discounted_amount < 1500:
    delivery_charge = 100.0
else:
    delivery_charge = 0.0

final_payable = discounted_amount + delivery_charge

print("\n" + "=" * 45)
print("               ORDER INVOICE")
print("=" * 45)
print(f"Subtotal             : Rs. {subtotal:.2f}")
print(f"Discount (10%)       : Rs. {discount:.2f}")
print(f"Amount after Discount: Rs. {discounted_amount:.2f}")
print(f"Delivery Charge      : Rs. {delivery_charge:.2f}")
print("-" * 45)
print(f"Final Payable Amount : Rs. {final_payable:.2f}")
print("=" * 45)
