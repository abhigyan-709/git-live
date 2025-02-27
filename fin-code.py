# Write a program to print the Fibonacci series up to n terms.

def fibonacciSeries(n: int):
    a = 0
    b = 1
    while (n > 0):
        print(a)
        temp = a + b
        a = b
        b = temp
        n -= 1

fibonacciSeries(10)