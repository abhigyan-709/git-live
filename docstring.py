#Write a python program to print the doc strings of the module. Hint - Design the module and then import them, to print the doc strings
import mymodule


print("Module Docstring:")
print(mymodule.__doc__)

# Print function docstrings
print("\nFunction Docstrings:")
print("add:", mymodule.add.__doc__)
print("subtract:", mymodule.subtract.__doc__)