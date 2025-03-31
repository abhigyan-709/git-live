import math

def area_of_t(a, b, c):
    if a + b >= c and a + c >= b and b + c >= a:
        s = (a + b + c) / 2 
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return "Invalid triangle sides"

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))


result = area_of_t(a, b, c)
print("Area of the triangle:",result)
