choice = int(input("Choose language:\n1. Python\n2. Java\n3. C++\n4. JavaScript\nEnter choice (1-4): "))
match choice:
    case 1:
        print("You chose Python")
    case 2:
        print("You chose Java")
    case 3:
        print("You chose C++")
    case 4:
        print("You chose JavaScript")
    case _:
        print("Invalid choice")
