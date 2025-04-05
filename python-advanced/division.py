# try, except, finally, else, raise

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2

    print("Rsult:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
except KeyboardInterrupt:
    print("Error: Program interrupted by user.")
else:
    print("Division completed successfully.")

finally:
    print("Execution completed.")