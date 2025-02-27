# Write a function that takes two numbers as input and returns their greatest common divisor (GCD).

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))