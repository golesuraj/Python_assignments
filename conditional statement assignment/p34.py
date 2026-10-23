year = int(input("Enter year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Century leap year")
    else:
        print("Century year, not a leap year")
else:
    if year % 4 == 0:
        print("Leap year, not a century year")
    else:
        print("Neither a leap year nor a century year")
