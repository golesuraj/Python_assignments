guest_name = input("Enter guest name: ")
room_type = input("Enter room type (Standard/Deluxe/Suite): ")
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Error: Number of nights must be greater than 0.")
else:
    if room_type.lower() == "standard":
        rate = 2000
    elif room_type.lower() == "deluxe":
        rate = 3500
    elif room_type.lower() == "suite":
        rate = 6000
    else:
        rate = 0

    if rate == 0:
        print("Error: Invalid room type entered.")
    else:
        room_charge = rate * nights
        if nights >= 10:
            discount_pct = 20
        elif nights >= 5:
            discount_pct = 10
        else:
            discount_pct = 0

        discount = (room_charge * discount_pct) / 100
        final_amount = room_charge - discount

        print("--- Hotel Booking Summary ---")
        print("Guest Name:", guest_name)
        print("Room Type:", room_type.capitalize())
        print("Number of Nights:", nights)
        print("Room Charge: Rs.", room_charge)
        print("Discount: Rs.", discount)
        print("Final Booking Amount: Rs.", final_amount)
