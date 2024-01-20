#Task 2
print("Simple Calculator")

while True:
    # Get user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Display operation choices
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    choice = input("Enter your choice (1, 2, 3, 4, 5): ")
    
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a valid option.")
        continue

    # Perform calculation based on user choice
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero. Please enter a non-zero second number.")
            continue
        result = num1 / num2
        operation = '/'

    # Display the result
    print(f"\nResult: {num1} {operation} {num2} = {result}\n")
