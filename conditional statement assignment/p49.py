status = input("Enter result code (P/F): ").strip().upper()
match status:
    case "P":
        print("Result: Pass")
    case "F":
        print("Result: Fail")
    case _:
        print("Invalid result code")
