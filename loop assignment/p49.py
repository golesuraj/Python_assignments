while True:
    print("--- Menu ---")
    print("1. Say Hello")
    print("2. Check Even or Odd")
    print("3. Exit")
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        name = input("Enter your name: ")
        print("Hello,", name)
    elif choice == "2":
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
