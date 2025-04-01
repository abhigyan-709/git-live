import math
def advanced_calculator():
    print("\nAdvanced Calculator\n")
    print("Select an operation:")
    print("1. Power (x^y)")
    print("2. Square Root (√x)")
    print("3. Sine (sin x)")
    print("4. Cosine (cos x)")
    print("5. Tangent (tan x)")
    choice = input("Enter choice (1-5): ")
    if choice == '1':
        x = float(input("Enter base number (x): "))
        y = float(input("Enter exponent (y): "))
        print(f"Result: {math.pow(x, y)}")
    elif choice == '2':
        x = float(input("Enter number (x): "))
        if x < 0:
            print("Error: Cannot compute square root of a negative number.")
        else:
            print(f"Result: {math.sqrt(x)}")
    elif choice == '3':
        x = float(input("Enter angle in degrees: "))
        print(f"Result: {math.sin(math.radians(x))}")
    elif choice == '4':
        x = float(input("Enter angle in degrees: "))
        print(f"Result: {math.cos(math.radians(x))}")
    elif choice == '5':
        x = float(input("Enter angle in degrees: "))
        print(f"Result: {math.tan(math.radians(x))}")
    else:
        print("Invalid choice! Please select a valid operation.")
advanced_calculator()