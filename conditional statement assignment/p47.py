role = input("Enter user role (admin/user/guest): ").strip().lower()
match role:
    case "admin":
        print("Full access")
    case "user":
        print("Limited access")
    case "guest":
        print("View only access")
    case _:
        print("Invalid role")
