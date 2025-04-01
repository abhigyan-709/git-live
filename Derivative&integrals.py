import sympy as sp
x = sp.Symbol('x')
f1 = x**3 + 5*x**2 - 3*x + 7
derivative_f1 = sp.diff(f1, x)
f2 = 4*x**3 - 2*x + 6
integral_f2 = sp.integrate(f2, x)
print("Derivative of f(x) = x^3 + 5x^2 - 3x + 7 is:", derivative_f1)
print("Integral of f(x) = 4x^3 - 2x + 6 is:", integral_f2, "+ C")  
