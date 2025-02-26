def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

a = int(input("Enter the number of terms: "))
fib(a)