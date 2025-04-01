import math
def herons_formula(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
if a + b > c and a + c > b and b + c > a:
    area = herons_formula(a, b, c)
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("Invalid triangle sides!")