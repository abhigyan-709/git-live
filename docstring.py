import my_module
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
# Print module docstring
print("Module Docstring:\n", my_module.__doc__)

# Print function docstrings
print("\nFunction Docstrings:")
print("add():", my_module.add.__doc__)
print("multiply():", my_module.multiply.__doc__)