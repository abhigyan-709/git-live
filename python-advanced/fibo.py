"""
This is the module-level docstring for the fibo file.
It contains functions for basic arithmetic operations.
"""

def add(a, b):
    """
    this is fibo file's docstring, 
    this takes 2 parameterized variable a, & b
    """
    return a + b

def main():
    """
    this is fibo file's docstring
    """
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    print("The value of the addition of two numbers will: ", add(a, b))
    

if __name__ == "__main__":
    main()