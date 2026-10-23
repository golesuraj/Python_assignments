choice = int(input("Menu:\n1. Pizza\n2. Burger\n3. Pasta\n4. Salad\nEnter choice (1-4): "))
match choice:
    case 1:
        print("You ordered Pizza")
    case 2:
        print("You ordered Burger")
    case 3:
        print("You ordered Pasta")
    case 4:
        print("You ordered Salad")
    case _:
        print("Invalid menu choice")
