name = input("Enter customer name: ")
plan = input("Enter plan type (Basic/Standard/Premium): ")
extra_data = float(input("Enter extra data used in GB: "))

if extra_data < 0:
    print("Error: Negative data usage is invalid.")
else:
    if plan.lower() == "basic":
        base_charge = 299
    elif plan.lower() == "standard":
        base_charge = 499
    elif plan.lower() == "premium":
        base_charge = 799
    else:
        base_charge = 0

    if base_charge == 0:
        print("Error: Invalid plan type selected.")
    else:
        extra_data_charge = extra_data * 20
        if extra_data > 10:
            surcharge = 100
        else:
            surcharge = 0

        final_bill = base_charge + extra_data_charge + surcharge

        print("--- Mobile Data Bill ---")
        print("Customer Name:", name)
        print("Plan Type:", plan.capitalize())
        print("Base Plan Charge: Rs.", base_charge)
        print("Extra Data Charge: Rs.", extra_data_charge)
        print("Surcharge: Rs.", surcharge)
        print("Final Bill: Rs.", final_bill)
