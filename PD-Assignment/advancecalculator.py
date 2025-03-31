#Design an advanced calculator using math module Features required - power, square root, trigonometry
import math

def power():
    base = float(input("Enter the base number: "))
    exponent = float(input("Enter the exponent: "))
    print(f"Result: {base}^{exponent} = {math.pow(base, exponent)}")

def square_root():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Error: Square root of a negative number is not real.")
    else:
        print(f"Square root of {num} = {math.sqrt(num)}")

def trigonometry():
    print("\nTrigonometry Options:")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    
    choice = input("Choose (1/2/3): ")
    angle = float(input("Enter the angle in degrees: "))
    radian = math.radians(angle)  

    if choice == '1':
        print(f"sin({angle}) = {math.sin(radian)}")
    elif choice == '2':
        print(f"cos({angle}) = {math.cos(radian)}")
    elif choice == '3':
        print(f"tan({angle}) = {math.tan(radian)}")
    else:
        print("Invalid choice!")

def main():
    while True:
        print("\nAdvanced Calculator:")
        print("1. Power Calculation (x^y)")
        print("2. Square Root (√x)")
        print("3. Trigonometry (sin, cos, tan)")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            power()
        elif choice == '2':
            square_root()
        elif choice == '3':
            trigonometry()
        elif choice == '4':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
