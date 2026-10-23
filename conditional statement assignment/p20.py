age = int(input("Enter age: "))
if age < 5:
    print("Ticket Price: Free")
elif age <= 12:
    print("Ticket Price: Rs. 10")
elif age <= 60:
    print("Ticket Price: Rs. 20")
else:
    print("Ticket Price: Rs. 15")
