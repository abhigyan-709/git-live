import math
"""Write a python program to calculate the area of triangle with the unequal sides.
 Hint - use heron's formula """
a=int(input("Enter The  Value Of A:"))
b=int(input("Enter The  Value Of B:"))
c=int(input("Enter The  Value Of C:"))
s=(a+b+c)/2
p=(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print(f"Area Of Triangle:{p}")
