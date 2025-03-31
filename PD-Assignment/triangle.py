#Write a python program to calculate the area of triangle with the unequal sides. Hint - use heron's formula
import math

def triangle_area(a, b, c):
  
    s = (a + b + c) / 2

  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area


a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))


if (a + b > c) and (a + c > b) and (b + c > a):
    print(f"The area of the triangle is: {triangle_area(a, b, c):.2f}")
else:
    print("Invalid triangle sides! The sum of any two sides must be greater than the third side.")
