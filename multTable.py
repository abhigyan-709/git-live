# Write a Python program to print the multiplication table of a given number.

def multTable(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

a = int(input("Enter the number: "))
multTable(a)
