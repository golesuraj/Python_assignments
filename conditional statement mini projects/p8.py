name = input("Enter customer name: ")
age = int(input("Enter age: "))
show_type = input("Enter show type (Morning/Evening): ")
day_type = input("Enter day type (Weekday/Weekend): ")

if age < 0:
    print("Error: Age cannot be negative.")
else:
    base_price = 200

    if age < 12:
        age_discount = base_price * 0.50
    elif age >= 60:
        age_discount = base_price * 0.30
    else:
        age_discount = 0

    if show_type.lower() == "morning":
        morning_discount = 30
    else:
        morning_discount = 0

    total_discount = age_discount + morning_discount

    if day_type.lower() == "weekend":
        surcharge = 50
    else:
        surcharge = 0

    final_price = base_price - total_discount + surcharge

    print("--- Movie Ticket Details ---")
    print("Customer Name:", name)
    print("Original Ticket Price: Rs.", base_price)
    print("Discount: Rs.", total_discount)
    print("Weekend Surcharge: Rs.", surcharge)
    print("Final Ticket Price: Rs.", final_price)
