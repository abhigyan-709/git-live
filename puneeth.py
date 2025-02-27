def add(x, y): 
    return x + y
def sub(x, y): 
    return x - y
def mult(x, y): 
    return x * y
def div(x, y):
    if y == 0: 
        return "Error! Division by zero." 
    return x / y


def calculator():
    print("Simple Calculator")

    while (True):
        print("Select operation:")
        print("To exit the calculator enter 'q'")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice = input("Enter choice: ")
        if (choice == 'q'):
            break
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if (choice == '1'):
                print(f'Result: {add(num1, num2)}')
            elif (choice == '2'):
                print(f'Result: {sub(num1, num2)}')
            elif (choice == '3'):
                print(f'Result: {mult(num1, num2)}')
            elif (choice == '4'):
                print(f'Result: {div(num1, num2)}')
        else: 
            print('Invalid operation')
calculator()