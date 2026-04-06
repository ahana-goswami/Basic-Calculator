print("=== Basic Calculator ===")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            print("Result:", num1 + num2)

        elif choice == '2':
            print("Result:", num1 - num2)

        elif choice == '3':
            print("Result:", num1 * num2)

        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print(" " \
                "Cannot divide by zero")

        else:
            print(" Invalid choice")

        again = input("\nContinue? (yes/no): ").lower()
        if again != "yes":
            print(" Calculator closed")
            break

    except ValueError:
        print(" Please enter valid numbers only!")