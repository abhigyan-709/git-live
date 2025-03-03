# # # defining a function
# # def fib(n):
# #     """Print the fibonacci series than a no. n"""
# #     a, b = 0, 1
# #     while a < n:
# #         print(a, end=', ')
# #         a, b = b, a+b
# #     print()

# # fib(1000)

# # def add(a, b):
# #     return a + b

# # print(add(5, 10))

# # def fib2(n = 10):
# #     fib_list = []
# #     a, b = 0, 1
# #     while a < n:
# #         fib_list.append(a)
# #         a, b = b, a+b
# #     return fib_list

# # fib100 = fib2(100)
# # print(fib100)

# def ask_ok(prompt, retries = 4, reminder="Please try again"):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'yes', 'yeah'}:
#             print("Thanks for letting me know")

#         if reply in {'n', 'no', 'nopes'}:
#             print("Ohh, sad to know!")

#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('Invalid User Response')
        
#         print(reminder)


# # TYPE 1 - only mandatory arguments
# ask_ok("Are you okay today?", retries=2, reminder="Try Again")


# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldnot ", action, end=' ')
#     print("if you will pass", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# args_parrot = {"voltage": 40000}

# parrot(**args_parrot)

def add(a, b=5, c=8.9):
    print("Value of b is ", b)
    print("value of c is ", c)
    print("If you will give value of a in function", a, "then it will be added.", end=' ')

value = {"a":10, "c": 10, "b": 11}

add(**value)


