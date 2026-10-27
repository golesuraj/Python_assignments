# Mini Project 4: Shopping Cart Total
# Problem Statement: Calculate a customer's shopping bill from multiple products.

print("=" * 45)
print("            SHOPPING CART BILLING")
print("=" * 45)

# Input validation for number of products
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
    
    # Validate price (non-negative)
    while True:
        try:
            price = float(input("  Enter price (Rs.): "))
            if price >= 0:
                break
            print("  Price cannot be negative. Try again.")
        except ValueError:
            print("  Invalid input! Enter a valid price.")

    # Validate quantity (must be positive integer)
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

# Calculate discount: 10% when subtotal is Rs. 3,000 or more
if subtotal >= 3000:
    discount = subtotal * 0.10
else:
    discount = 0.0

discounted_amount = subtotal - discount

# Delivery charge: Rs. 100 if discounted amount is below Rs. 1,500; otherwise free
if discounted_amount < 1500:
    delivery_charge = 100.0
else:
    delivery_charge = 0.0

final_payable = discounted_amount + delivery_charge

# Display Final Bill
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
